'''
consumer.py
Created on 2019/5/14 10:36
Copyright (c) 2019/5/14
@author: hly
'''
import threading
import time
import random
from commons import base_consumer_action
from util.log_util import LogUtil


class Consumer(threading.Thread):
    """
    消费者线程，主要任务是执行拿到的消费动作
    """
    # 消费动作失败之后重新尝试的次数，可供外面访问
    _WORK_TRY_NUM = 0

    def __init__(self, queue, name, sleep_time, work_try_num):
        """
        初始化消费者线程
        :param queue: 使用的队列
        :param name: 消费者线程的名称
        :param sleep_time: 执行下一次消费者休息的时间
        :param work_try_num: 每个消费动作允许失败的次数
        """
        super(self.__class__, self).__init__()
        self.queue = queue
        self.name = name
        self.sleep_time = sleep_time
        self.work_try_num = work_try_num
        Consumer._WORK_TRY_NUM = work_try_num
        # 初始化日志
        self.logger = LogUtil().get_logger("comsumer_%s" % self.name, "comsumer_%s" % self.name)

    def run(self):
        while True:
            try:
                # 从线程中得到一个消费动作，其在队列中的状态由new转为work
                action = self.queue.get()
                if not isinstance(action, base_consumer_action.ConsumerAction):
                    raise Exception('Action not Consumer base')

                # 任务下一次消费动作随机休息的时长，最长不超过设置的上限sleep_time
                sleep_time = random.randint(1, self.sleep_time * 10) * 0.1
                time.sleep(sleep_time)

                action.consumer_thread_name = self.name
                start_time = time.clock()
                # 执行得到消费动作
                re = action.action()
                end_time = time.clock()

                # 计算执行消费动作的时间
                work_sec = int(round((end_time - start_time)))

                # 输出消费线程的日志
                self.logger.info("queue name %s finish,sleep time %s\'s,action time %s\'s,"
                             "action retry %s times,result:%s" % \
                             (self.name, sleep_time, work_sec, action.try_num, re.__str__() if re is not None else ''))

                # 根据消费动作的结果和该消费动作的失败次数，决定是否再次放入队列中重新尝试
                if not re[0] and action.try_num < self.work_try_num:
                    # 该消费动作的失败次数累加
                    action.try_num += 1
                    # 向队列中放入消费动作，其中队列中的状态为new
                    self.queue.put(action)
                # 把得到的消费动作的状态在队列中从work转为done
                self.queue.task_done()
            except:
                self.logger.exception()

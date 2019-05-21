'''
text_pro_con_demo.py  生成消费队列的测试
Created on 2019/5/21 19:47
Copyright (c) 2019/5/21
@author: hly
'''
from commons import base_consumer_action
from commons import base_producer_action
from commons import consumer
from commons import producer
import queue


class ConsumerAction(base_consumer_action.ConsumerAction):

    def __init__(self, text):
        '''
        初始化消费者实现类

        :param text:     消费者要处理的数据
        '''
        super(self.__class__, self).__init__()
        self.text = text

    def action(self):
        '''
        消费者的具体需求实现

        :return:       消费动作的处理结果，用于消费者线程的日志打印
        '''
        result = True
        r_test = ''
        try:
            r_test = self.text
        except:
            result = False

        return self.result(result, [r_test])

    def fail_action(self, values):
        if self.try_num >= consumer.Consumer._WORK_TRY_NUM:
            pass

    def success_action(self, values):
        pass


class ProducerAction(base_producer_action.ProducerAction):

    def queue_items(self):
        '''
        生成指定的消费者动作

        :return:        消费者动作的集合
        '''
        list = []
        for i in range(0, 200):
            c = ConsumerAction(i)
            list.append(c)
        return list


if __name__ == "__main__":
    # 初始化使用的队列
    q = queue.Queue()
    # 初始化生产者动作
    pp = ProducerAction()
    # 初始化生产者
    p = producer.Producer(q, pp, "hly_queue", 2, 60, 1, 2)
    # 启动整个生产和消费任务
    p.start_work()

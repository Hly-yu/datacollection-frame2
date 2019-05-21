'''
base_producer_action.py
Created on 2019/5/14 9:46
Copyright (c) 2019/5/14
@author: hly
'''


class ProducerAction:
    """
    生产动作基类
    生产 消费动作（consumerAction） 实例列表
    """

    def queue_time(self):
        """
        制定 生产动作对象（ProducerAction） 生产 消费动作（ConsumerAction）实例列表 的规则,
        具体的生产逻辑由子类去实现
        :return:消费动作实例列表
        """
        pass

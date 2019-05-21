'''
base_consumer_action.py  消费动作基类
Created on 2019/5/14 9:52
Copyright (c) 2019/5/14
@author: hly
'''


class ConsumerAction(object):
    """
    消费动作基类
    """

    def __init__(self):
        """
        :param try_num 当前消费动作失败的重试次数
        """
        self.try_num = 1
        self.consumer_thread_name = ''

    def action(self):
        """
        制定消费动作的执行规则，子类实现具体的消费逻辑
        :return:
        """
        pass

    def result(self, is_success, values):
        """
        action()返回调用的方法
        :param success_flag: True:成功 False:失败
        :param values: []
        :return: [true,1,2,3,4]
        """
        result_value = []
        result_value.append(is_success)
        if not is_success:
            self.fail_action(values)
        else:
            self.success_action(values)

        for re in values:
            result_value.append(re)

        return result_value

    def success_action(self, values):
        """
        action()执行成功返回结果前的逻辑处理
        :return:
        """
        pass

    def fail_action(self, values):
        """
        action(),执行失败返回结果前的逻辑处理
        :return:
        """
        pass

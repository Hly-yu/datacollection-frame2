'''
log_util.py 日志
Created on 2019/5/14 9:52
Copyright (c) 2019/5/14
@author: hly
'''

from configs import config
from logging.handlers import TimedRotatingFileHandler
import logging, os
from util import content


class LogUtil:
    base_logger = content._NULL_STR

    log_dict = {}

    def get_base_logger(self):
        if LogUtil.base_logger == content._NULL_STR:
            LogUtil.base_logger = self.__get_logger('info', 'info')
        return LogUtil.base_logger

    def get_logger(self, log_name, file_name):
        key = log_name + file_name
        if key not in LogUtil.log_dict:
            LogUtil.log_dict[key] = self.__get_logger(log_name, file_name)

        return LogUtil.log_dict[key]

    def __get_new_logger(self, log_name, file_name):
        l = LogUtil()
        l.__get_logger(log_name, file_name)
        return l

    def __get_logger(self, log_name, file_name):
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.INFO)

        fh = TimedRotatingFileHandler(config._LOG_DIR % (file_name), 'D')
        fh.suffix = "%Y%m%d.log"
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        return self

    def info(self, msg):
        self.logger.info(msg)
        self.logger.handlers[0].flush()

    def error(self, msg):
        self.logger.error(msg)
        self.logger.handlers[0].flush()

    def exception(self, msg='Exception Logged'):
        self.logger.exception(msg)
        self.logger.handlers[0].flush()


# if __name__ == '__main__':
#     b = LogUtil().get_logger("producer", "producer")
#     b.info("111")
#     b.error("222")
#     aa = os.getcwd()
#     print(aa)
#     try:
#         1 / 0
#     except:
#         b.exception()

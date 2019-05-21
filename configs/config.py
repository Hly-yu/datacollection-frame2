'''
config.py  参数
Created on 2019/1/4 9:29
Copyright (c) 2019/1/4.
@author: hly
'''
# 日志地址
_LOG_DIR = "E:\大数据学习\何老师\python\项目2\datacollection-frame2\log\%s"

# 数据库配置_测试
_TEST_LOCAL_DB = {'HOST': 'localhost', 'USER': 'root', 'PASSWD': '12345678', 'DB': 'test', 'CHARSET': 'utf8', 'PORT': 3306}

# 集群配置_测试
_DB_TEST = {'HOST': '192.168.88.195', 'PORT': 3306, 'USER': 'hainiu', 'PASSWD': '12345678', 'DB': 'hainiutest',
            'CHARSET': 'utf8'}
              #host="192.168.88.195", user="hainiu", passwd="12345678", db="hainiutest",charset="utf8", port=3306

# NAME, P_SLEEP_TIME, C_MAX_NUM, C_MAX_SLEEP_TIME, C_RETRY_TIMES
_QUEUE_DEMO = {'NAME': 'demo', 'P_SLEEP_TIME': 5, 'C_MAX_NUM': 3, 'C_MAX_SLEEP_TIME': 3, 'C_RETRY_TIMES': 3}

"""
生产者线程初始化参数
:param NAME:             线程名称
:param P_SLEEP_TIME:     生产线程每多长时间工作一次
:param C_MAX_NUM:        消费线程的最大线程数
:param C_MAX_SLEEP_TIME: 消费线程工作间隔最大休眠时间
:param C_RETRY_TIMES:    消费动作对象action 最大重试次数
"""
_QUEUE_TEST = {'NAME': 'hainiu', 'P_SLEEP_TIME': 3, 'C_MAX_NUM': 1,
               'C_MAX_SLEEP_TIME': 1, 'C_RETRY_TIMES': 3, 'MAX_FAIL_TIMES': 6,
               'LIMIT_NUM': 2}

# 数据地址
_LOCAL_DATA_DIR = '/Users/leohe/Data/python/hainiu_cralwer/data/%s'

# 报警电话
_ALERT_PHONE = '110'

# 下载任务配置_测试
_DOWN_CONFIG = {'QUERY_LIMIT': 20, 'QUERY_FAIL_TIMES': 6, 'WORK_THREAD_NUMS': 5, 'QUEUE_SLEEP_TIMES': 2,
                'WORK_SLEEP_TIMES': 3, 'FAIL_RETRY_TIMES': 2, 'FILE_FLAG': 'one'}

# 下载任务配置
# _DOWN_CONFIG = {'QUERY_LIMIT':20,'FILE_FLAG':'one','QUERY_FAIL_TIMES':6,'WORK_THREAD_NUMS':10,'QUEUE_SLEEP_TIMES':1,'WORK_SLEEP_TIMES':3,'FAIL_RETRY_TIMES':2}

# 查找新闻任务配置_测试
_FIND_NEWS_CONFIG = {'QUERY_LIMIT': 1, 'QUERY_FAIL_TIMES': 6, 'WORK_THREAD_NUMS': 1, 'QUEUE_SLEEP_TIMES': 1,
                     'WORK_SLEEP_TIMES': 3, 'FAIL_RETRY_TIMES': 2,'FILE_FLAG': 'one'}

# 查找新闻任务配置
# _FIND_NEWS_CONFIG = {'QUERY_LIMIT':10,'QUERY_FAIL_TIMES':6,'WORK_THREAD_NUMS':5,'QUEUE_SLEEP_TIMES':1,'WORK_SLEEP_TIMES':3,'FAIL_RETRY_TIMES':2}

# KAFKA队列配置
_KAFKA_CONFIG = {'HOST': 'nn1.hadoop:9092,nn2.hadoop:9092,s1.hadoop:9092', 'TOPIC': 'hainiu_html_class4'}



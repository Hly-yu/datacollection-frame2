'''
find_queue.py
Created on 2019/5/21 20:03
Copyright (c) 2019/5/21
@author: hly
'''

import sys
from util.db_util import DBUtil
from util.log_util import LogUtil
from configs import config
from tld import get_fld
import time
import random
import json
import io


def push_queue_items():
    count_news_seed_sql = """select count(1) from bigdata_web_seed where status = 0;"""
    select_news_seed_sql = """select url,category,last_crawl_time from bigdata_web_seed where status=0 limit %s,%s;"""
    insert_news_seed_queue_items_sql = """insert into bigdata (type,action,params) """


if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
    push_queue_items()

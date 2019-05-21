'''
db_util.py
Created on 2019/5/21 20:04
Copyright (c) 2019/5/21
@author: hly
'''
from configs import config
import pymysql


class DBUtil:

    def __init__(self, db):
        self.db = pymysql.connect(host=db['HOST'], user=db['USER'], passwd=db['PASSWD'], db=db['DB'],
                                  charset=db['CHARSET'], port=db['PORT'])

    def read_one(self, sql):
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def read_tuple(self, sql):
        """execute sql return tuple
        select a,b,c from table
        ((a,b,c),(a,b,c))
        """
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def read_dict(self, sql):
        """execute sql return dict
        select a,b,c from table
        ({a:1,b:2,c:33},{a:1,b:3,c:45})
        """
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def executemany(self, sql, values):
        '''
        insert into table (a,b,c) values(?,?,?)
        values   [(1,2,3),(324,6,1),(11,5,5)]
        :return:
        '''
        self.cursor = self.db.cursor()
        self.cursor.executemany(sql, values)
        self.db.commit()

    def executemany_no_commit(self, sql, values):
        self.cursor = self.db.cursor()
        self.cursor.executemany(sql, values)

    def execute(self, sql):
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)
        self.db.commit()

    def execute_no_commit(self, sql):
        self.cursor = self.db.cursor()
        self.cursor.execute(sql)

    def commit(self):
        self.db.commit()

    def close(self):
        """close db connect
        """
        self.cursor = self.db.cursor()
        self.cursor.close()
        self.db.close()

    def rollback(self):
        """rollback db connect
        """
        self.db.rollback()

    def rollback_close(self):
        """rollback and close db connect
        """
        self.db.rollback()
        self.db.close()


if __name__ == '__main__':
    db = DBUtil(config._TEST_LOCAL_DB)

    # sql = """
    # insert into bigdata_queue
    #     (type,action,params,fail_ip,create_times)
    #     values (1,"10153108084201229","Baltimore Ravens","Sports Team","2015-08-04 21:35:40");
    # """
    # for i in range(0,1):
    #     db.execute(sql)

    dataT = db.read_dict("select id,action,params from bigdata_queue where type=1 limit 0,1 for update;")
    for objs in dataT:
        print(objs)

    id = dataT[0]["id"]

    print(id)
    #
    # sql = "update bigdata_queue set type=0 where id=%s" % id
    # db.execute_no_commit(sql)
    # db.commit()
    #
    # db.close()

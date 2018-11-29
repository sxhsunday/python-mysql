#!/usr/bin/python
# -*- coding:utf8 -*-
import pymysql
import sys
if sys.getdefaultencoding() != 'gbk':
    reload(sys)
    sys.setdefaultencoding('gbk')



db = pymysql.connect("localhost","root","1121","bbs")
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
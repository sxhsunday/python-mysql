#!/usr/bin/python
# -*- coding:utf8 -*-
import pymysql
import sys
if sys.getdefaultencoding() != 'gbk':
    reload(sys)
    sys.setdefaultencoding('gbk')



db = pymysql.connect("localhost","root","1121","bbs")
cursor = db.cursor()
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
# sql ="UPDATA EMPLOYEE set AGE = AGE + 1 WHERE SEX = M"
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
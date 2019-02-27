#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:2019/1/30
时间:10:10
"""
import cx_Oracle
import os
os.environ["NLS_LANG"] = "RUSSIAN_RUSSIA.AL32UTF8"
print(cx_Oracle.__version__)
db = cx_Oracle.connect('system', 'oracle', '192.168.99.100:1521/XE')
print(db.version)
print(db.dsn)
# 获取游标
cursor = db.cursor()
result = cursor.execute("select * from  CDGAS_QLFX_BASE")
print(list(result))
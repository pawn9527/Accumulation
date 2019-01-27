#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:2019/1/27
时间:10:20
"""
# 拒绝隐式引用 因为文件名称和celery包名称冲突.
from __future__ import absolute_import
from celery import Celery

app = Celery('Celery', include=['Celery.tasks'])
app.config_from_object('Celery.celery_config')

if __name__ == '__main__':
    app.start()

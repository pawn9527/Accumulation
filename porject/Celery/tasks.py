#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:2019/1/27
时间:10:21
"""
from __future__ import absolute_import
from porject.Celery.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def add(x, y):
    return x + y


@app.task(bind=True)
def div(self, x, y):
    logger.info('Executing task id {0.id}, args: {0.args!r}'
                'kwargs: {0.kwargs!r}'.format(self.request))
    
    try:
        result = x / y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=5, max_retries=3)
    
    return result

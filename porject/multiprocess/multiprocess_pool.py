#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:2018/12/19
时间:16:36
"""
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print(f"Run task  {name} ({os.getpid()})")
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f"Task {name} run {end - start} seconds")


if __name__ == '__main__':
    print(f"Parent process {os.getpid()}")
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    
    p.close()
    # 可以等待 子进程结束后再继续往下进行, 通常可以进行进程间的同步
    p.join()
    # Pool 对象调用 join() 方法会等待所有的子进程执行完毕, 调用 join() 之前必须调用 close(), 就不能添加新的 Process
    

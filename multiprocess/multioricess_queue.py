#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:2018/12/19
时间:16:53
"""
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码

def write(q):
    for value in ["A", "B", "C"]:
        print(f"Put {value} to queue")
        q.put(value)
        time.sleep(random.random())


# 读数进程的代码
def read(q):
    while True:
        value = q.get()
        print(f"Get {value} from queue")


if __name__ == '__main__':
    # 父进程创建Queue 并且传递给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw, 写入
    pw.start()
    # 启动子进程pr, 读取
    pr.start()
    # 等待pw 结束
    pw.join()
    # pr 进程里是死循环, 无法等待其结束, 只能强行终止
    pr.terminate()

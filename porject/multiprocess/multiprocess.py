#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:2018/12/19
时间:16:20
"""
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    # 子进程的进程id
    print(f"Run child process {name}  ({os.getpid()})")


if __name__ == '__main__':
    # 主进程的进程id
    print(f"Parent process {os.getpid()}")
    p = Process(target=run_proc, args=('test',))
    print("Process will start")
    p.start()
    p.join()
    print("Process end")

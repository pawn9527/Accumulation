#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:18-10-11
时间:上午10:16
"""
import numpy as np
import matplotlib as plt
import time


# https://legacy.gitbook.com/book/yoyoyohamapi/mit-ml/details

def exeTime(func):
    """
    耗时计算装饰器
    """

    def newFunc(*args, **kwargs):
        first_time = time.time()
        back = func(*args, **kwargs)
        return back, time.time() - first_time

    return newFunc


def loadDataSet(filename):
    """
    读取数据
    数据格式如下:
    "feature1 TAB feature2 TAB feature3 TAB label"
    Args:
        filename: 文件名
    Returns:
        x: 训练样本集矩阵
        y: 标签矩阵
    """
    numFeat = len(open(filename).readline().split('\t')) - 1
    X = []
    y = []
    file = open(filename)
    for line in file.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        X.append(lineArr)
        y.append(float(curLine[-1]))
    return np.mat(X), np.mat(y).T


def h(theta, x):
    """
    预测函数
    :param theta: 相关系数矩阵
    :param x: 特征向量
    :return: 预测结果
    """
    return (theta.T * x)[0, 0]


def J(theta, X, y):
    """
    代价函数
    :param theta: 相关系数矩阵
    :param X: 样本集矩阵
    :param y: 标签集矩阵
    :return: 预测误差（代价）
    """
    m = len(X)
    return (X * theta - y).T * (X * theta - y) / (2 * m)


@exeTime
def bgd(rate, maxLoop, epsilon, X, y):
    """
    批量梯度下降
    :param rate:学习率
    :param maxLoop: 最大迭代数
    :param epsilon: 收敛精度
    :param X: 样本矩阵
    :param y: 标签矩阵
    :return: (theta, errors, thetas), timeConsumed
    """
    m, n = X.shape
    # 初始化 theta
    count = 0
    converged = False
    error = float('inf')
    errors = []
    thetas = {}
    for j in range(n):
        thetas[j] = [thetas[j, 0]]
    while count <= maxLoop:
        if converged:
            break
        count = count + 1
        for j in range(n):
            deriv = (y - X * thetas).T * X[:, j] / m
            thetas[j, 0] = thetas[j, 0] + rate * deriv
            thetas[j].append(thetas[j, 0])
        error = J(thetas, X, y)
        errors.append(error[0, 0])
        # 如果已经收敛
        if (error < epsilon):
            converged = True
    return thetas, errors, thetas

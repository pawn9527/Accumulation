#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:18-9-10
时间:上午9:16
"""
import xlwt
from random import randint

from xlwt import Worksheet

from collections import defaultdict

work_book = xlwt.Workbook(encoding='utf-8')

work_sheet = work_book.add_sheet('Line Dance')  # type: Worksheet

DATA = {'age': [{'name': '<15岁', 'square': 20, 'line': 20},
                {'name': '15-29岁', 'square': 43, 'line': 25},
                {'name': '30-44岁', 'square': 36, 'line': 28},
                {'name': '45-59岁', 'square': 49, 'line': 65},
                {'name': '59>岁', 'square': 96, 'line': 35}],
        'job': [{'name': '学生', 'square': 17, 'line': 56},
                {'name': '职员', 'square': 38, 'line': 43},
                {'name': '自由职业', 'square': 44, 'line': 20},
                {'name': '无业', 'square': 17, 'line': 24},
                {'name': '其他', 'square': 41, 'line': 16}],
        'join_time': [{'name': '小于1年', 'line': 46, 'square': 22},
                      {'name': '1-3年', 'line': 62, 'square': 72},
                      {'name': '3-5年', 'line': 41, 'square': 52},
                      {'name': '大于5年', 'line': 96, 'square': 128}],
        'once_time': [{'name': '小于45分钟', 'square': 67, 'line': 19},
                      {'name': '45--60分钟', 'square': 46, 'line': 51},
                      {'name': '60--90分钟', 'square': 35, 'line': 43},
                      {'name': '120分钟', 'square': 48, 'line': 19},
                      {'name': '大于120分钟', 'square': 64, 'line': 27}],
        'times_of_weak': [{'name': '每天多次', 'square': 16, 'line': 48},
                          {'name': '每天1次', 'square': 48, 'line': 20},
                          {'name': '每周4-5', 'square': 41, 'line': 33},
                          {'name': '每周2-3', 'square': 24, 'line': 44},
                          {'name': '每周1次', 'square': 80, 'line': 48},
                          {'name': '其他', 'square': 22, 'line': 80}],
        'know_of_way': [{'name': '书刊,杂志', 'square': 6, 'line': 0},
                        {'name': '媒体(互联网, 手机)', 'square': 35, 'line': 23},
                        {'name': '朋友介绍', 'square': 64, 'line': 46},
                        {'name': '亲身参与培训, 比赛', 'square': 45, 'line': 81}],
        'join_of_way': [{'name': '视频学习', 'square': 33, 'line': 23},
                        {'name': '群众组织', 'square': 59, 'line': 17},
                        {'name': '参与专门的培训', 'square': 38, 'line': 69},
                        {'name': '参与各级比赛', 'square': 20, 'line': 41}]
        }


class PaperData:
    def __init__(self, sheet, dance_type, data):
        self._sheet = sheet
        self._type = dance_type
        self._data = data
        self._row_data = []
        self._head = [
            '年龄区间', '职业',
            '参与年限', '单次时长', '每周频次',
            '了解途径', '参与途径'
        ]

        self._cant_select_dict = {key: [] for key in self._data.keys()}

    def get_random(self, index, last, key):
        number = randint(index, last - 1)
        if number in self._cant_select_dict[key]:
            if len(self._cant_select_dict[key]) >= len(self._data[key]) - 1:
                return number
            else:
                return self.get_random(index, last, key)
        else:
            return number

    # def decrease_once_all(self):
    #     self._cant_select_dict = {
    #         key: self._cant_select_dict[key] - 1
    #         for key in self._cant_select_dict.keys()
    #     }

    def format_data(self):
        for row in range(1, 161):
            data_list = []
            for key, value in self._data.items():
                number = self.get_random(0, len(value), key)
                data_list.append(value[number]['name'])
                self._data[key][number][self._type] = self._data[key][number][self._type] - 1
                if self._data[key][number][self._type] <= 0:
                    self._cant_select_dict[key].append(number)
            self._row_data.append(data_list)

    def write_xlt(self):
        if not self._row_data:
            self.format_data()
        # 先给xlt 写入头部
        for index, key in enumerate(self._head):
            work_sheet.write(0, index, key)
        # 写入 160 行有规律的数据
        for row, value in enumerate(self._row_data):
            for col, name in enumerate(value):
                work_sheet.write(row + 1, col, name)
        work_book.save(f'{self._type}_dance.xls')


if __name__ == '__main__':
    paper = PaperData(
        sheet="Line Dance",
        dance_type='square',
        data=DATA
    )
    paper.format_data()
    paper.write_xlt()

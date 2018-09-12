# coding=utf-8
from datetime import datetime

import xlwt
from xlwt import Worksheet
from random import randint

age_mapping = {
    1: {'age': '<15岁', 'square': 0.13, 'line': 0.13, 'use_count': 0},
    2: {'age': '15-29岁', 'square': 0.27, 'line': 0.16, 'use_count': 0},
    3: {'age': '30-44岁', 'square': 0.23, 'line': 0.18, 'use_count': 0},
    4: {'age': '45-59岁', 'square': 0.31, 'line': 0.41, 'use_count': 0},
    5: {'age': '59>岁', 'square': 0.6, 'line': 0.22, 'use_count': 0}
}

job_mapping = {
    1: {'job': '学生', 'square': 0.11, 'line': 0.35, 'use_count': 0},
    2: {'job': '职员', 'square': 0.24, 'line': 0.27, 'use_count': 0},
    3: {'job': '自由职业', 'square': 0.28, 'line': 0.13, 'use_count': 0},
    4: {'job': '无业', 'square': 0.11, 'line': 0.15, 'use_count': 0},
    5: {'job': '其他', 'square': 0.26, 'line': 0.10, 'use_count': 0},
}

join_time_mapping = {
    1: {'time': '小于1年', 'line': 0.29, 'square': 0.14, 'use_count': 0},
    2: {'time': '1-3年', 'line': 0.39, 'square': 0.45, 'use_count': 0},
    3: {'time': '3-5年', 'line': 0.26, 'square': 0.33, 'use_count': 0},
    4: {'time': '大于5年', 'line': 0.6, 'square': 0.8, 'use_count': 0}
}

once_time_mapping = {
    1: {'mince': '小于45分钟', 'square': 0.42, 'line': 0.12, 'use_count': 0},
    2: {'mince': '45--60分钟', 'square': 0.29, 'line': 0.32, 'use_count': 0},
    3: {'mince': '60--90分钟', 'square': 0.22, 'line': 0.27, 'use_count': 0},
    4: {'mince': '120分钟', 'square': 0.3, 'line': 0.12, 'use_count': 0},
    5: {'mince': '大于120分钟', 'square': 0.4, 'line': 0.17, 'use_count': 0},
}

times_of_weak_mapping = {
    1: {'count': '每天多次', 'square': 0.10, 'line': 0.3, 'use_count': 0},
    2: {'count': '每天1次', 'square': 0.30, 'line': 0.13, 'use_count': 0},
    3: {'count': '每周4-5', 'square': 0.26, 'line': 0.21, 'use_count': 0},
    4: {'count': '每周2-3', 'square': 0.15, 'line': 0.28, 'use_count': 0},
    5: {'count': '每周1次', 'square': 0.5, 'line': 0.30, 'use_count': 0},
    6: {'count': '其他', 'square': 0.14, 'line': 0.5, 'use_count': 0},
}

know_the_way_mapping = {
    1: {'way': '书刊,杂志', 'square': 6, 'line': 0},
    2: {'way': '媒体(互联网, 手机)', 'square': 35, 'line': 23},
    3: {'way': '朋友介绍', 'square': 64, 'line': 46},
    4: {'way': '亲身参与培训, 比赛', 'square': 45, 'line': 81},
}

join_way_mapping = {
    1: {'way': '视频学习', 'square': 33, 'line': 23},
    2: {'way': '群众组织', 'square': 59, 'line': 17},
    3: {'way': '参与专门的培训', 'square': 38, 'line': 69},
    4: {'way': '参与各级比赛', 'square': 20, 'line': 41},
}

liking_degree_mapping = {
    1: {'degree': '非常喜欢', 'square': 83, 'line': 63},
    2: {'degree': '比较喜欢', 'square': 56, 'line': 54},
    3: {'degree': '一般', 'square': 11, 'line': 31},
    4: {'degree': '不太喜欢', 'square': 0, 'line': 2},
    5: {'degree': '非常不喜欢', 'square': 0, 'line': 0},
}

square_dance_title = [
    {
        '个人信息': [
            '年龄区间',
            '性别',
            '职业',
            '文化程度'
        ],
        '个人参与与体验情况': [
            '排舞内在动机',
            '排舞外在动机',
            '了解途径',
            '参与方式',
            '锻炼年限',
            '参与频率',
            '单次时长',
            '参与场地',
            '室内外对比'
            '对于器材的满意程度'
        ],
        '项目体验评价': [
            '音乐风格',
            '上肢动作是否明确规定',
            '下肢动作是否明确规定',
            '完成动作时候的行为态度',
            '动作的难度区分程度',
            '喜欢程度'
        ]
    }
]

line_dance_title = {
    '个人信息': [
        '年龄区间',
        '性别',
        '职业',
        '文化程度'
    ],
    '个人参与与体验情况': [
        '排舞内在动机',
        '排舞外在动机',
        '了解途径',
        '参与方式',
        '锻炼年限',
        '参与频率',
        '单次时长',
        '参与场地',
        '室内外对比'
        '对于器材的满意程度'
    ],
    '项目体验评价': [
        '音乐风格',
        '上肢动作是否明确规定',
        '下肢动作是否明确规定',
        '完成动作时候的行为态度',
        '动作的难度区分程度',
        '喜欢程度'
    ]

}

need_data = [
    '年龄区间', '职业',
    '参与年限', '单次时长', '每周频次',
    '了解途径', '参与途径', '喜欢程度'
]

work_book = xlwt.Workbook(encoding='utf-8')

work_sheet = work_book.add_sheet('Line Dance')  # type: Worksheet

for row, key in enumerate(need_data):
    work_sheet.write(0, row, key)


def get_random(index, last, not_number=None):
    if not not_number:
        not_number = []
    number = randint(index, last)
    if number in not_number:
        get_random(index, last, not_number)
    else:
        return number


for index in range(1, 161):
    for row, key in enumerate(need_data):
        if key == "年龄区间":
            age_user_list = []
            select = get_random(1, 5, age_user_list)
            work_sheet.write(index, row, age_mapping[select]['age'])
            age_mapping[select]['use_count'] = age_mapping[select]['use_count'] + 1
            if age_mapping[select]['line'] * 160 >= age_mapping[select]['use_count']:
                age_user_list.append(select)
        elif key == "职业":
            age_user_list = []
            select = get_random(1, 5, age_user_list)
            work_sheet.write(index, row, job_mapping[select]['job'])
            job_mapping[select]['use_count'] = job_mapping[select]['use_count'] + 1
            if job_mapping[select]['line'] * 160 >= job_mapping[select]['use_count']:
                age_user_list.append(select)
        elif key == "参与年限":
            age_user_list = []
            select = get_random(1, 4, age_user_list)
            work_sheet.write(index, row, join_time_mapping[select]['time'])
            join_time_mapping[select]['use_count'] = join_time_mapping[select]['use_count'] + 1
            if join_time_mapping[select]['line'] * 160 >= join_time_mapping[select]['use_count']:
                age_user_list.append(select)
        elif key == "单次时长":
            age_user_list = []
            select = get_random(1, 5, age_user_list)
            work_sheet.write(index, row, once_time_mapping[select]['mince'])
            once_time_mapping[select]['use_count'] = once_time_mapping[select]['use_count'] + 1
            if once_time_mapping[select]['line'] * 160 >= once_time_mapping[select]['use_count']:
                age_user_list.append(select)
        elif key == "每周频次":
            age_user_list = []
            select = get_random(1, 6, age_user_list)
            work_sheet.write(index, row, times_of_weak_mapping[select]['count'])
            times_of_weak_mapping[select]['use_count'] = times_of_weak_mapping[select]['use_count'] + 1
            if times_of_weak_mapping[select]['line'] * 160 >= times_of_weak_mapping[select]['use_count']:
                age_user_list.append(select)
        elif key == "了解途径":
            age_user_list = []
            select = get_random(1, 4, age_user_list)
            work_sheet.write(index, row, know_the_way_mapping[select]['way'])
            know_the_way_mapping[select]['line'] = know_the_way_mapping[select]['line'] - 1
            if know_the_way_mapping[select]['line'] <= 0:
                age_user_list.append(select)
        elif key == "参与途径":
            age_user_list = []
            select = get_random(1, 4, age_user_list)
            work_sheet.write(index, row, join_way_mapping[select]['way'])
            join_way_mapping[select]['line'] = join_way_mapping[select]['line'] - 1
            if join_way_mapping[select]['line'] <= 0:
                age_user_list.append(select)
        elif key == "喜欢程度":
            age_user_list = []
            select = get_random(1, 5, age_user_list)
            work_sheet.write(index, row, liking_degree_mapping[select]['degree'])
            liking_degree_mapping[select]['line'] = liking_degree_mapping[select]['line'] - 1
            if liking_degree_mapping[select]['line'] <= 0:
                age_user_list.append(select)
work_book.save('line_dance.xls')

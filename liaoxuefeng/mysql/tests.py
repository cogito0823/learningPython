#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   tests.py
@Time    :   2020/04/09 00:51:57
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   None
'''

import os

test_list = {'SQL的全称是':'Structure Query Language',
             'DDL的全称是':'Data Definition Language',
             'DML的全称是':'Data Manipulation Language',
             'DQL的全称是':"Data Query Language"}

def do_test(num, question, answer):
    print(f'\n{num}. {question}:\n')
    reply = input()
    if reply == 'q':
        os._exit(0)
    if reply.lower() != answer.lower():
        return f'{question}?'

if __name__ == "__main__":       
    print('\n*********************************')
    print('Welcome to mysql tests!\n')
    sum = len(test_list)
    print(f"There are {sum} questions. You can enter 'q' to exit at any time.")
    i = 1
    result = []
    for question, answer in test_list.items():
        judge = do_test(i, question, answer)
        if judge:
            result.append(judge)
        i += 1
    
    count_wrong = len(result)
    print(f'\n*********************************\nYou have {count_wrong} Errors. Your wrong tests results is:\n')
    for judge in result:
        print(judge)
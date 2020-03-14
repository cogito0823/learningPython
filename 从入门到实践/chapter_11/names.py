#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   names.py
@Time    :   2020/03/14 15:46:06
@Author  :   cogito0823
@Contact :   754032908@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import name_function

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPlease give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print('\tNeatly formatted name: ' + formatted_name + '.')
    
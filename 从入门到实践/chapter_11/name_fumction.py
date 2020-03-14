#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   name_fumction.py
@Time    :   2020/03/14 15:44:21
@Author  :   cogito0823
@Contact :   754032908@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

def get_formatted_name(first,last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()
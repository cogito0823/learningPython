#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   city_functions.py
@Time    :   2020/03/14 21:55:39
@Author  :   cogito0823
@Contact :   754032908@qq.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

def get_city_country(city,country,population=''):
    """生成城市，国家字符串"""
    if population:
        return("{}, {} - population {}".format(city,country,population))
    else:
        return("{}, {}".format(city,country))

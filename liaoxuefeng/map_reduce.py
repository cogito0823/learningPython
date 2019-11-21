#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: map_reduce.py
# Created on : 2019-11-17 14:51:55
# Author: cogito0823
# Last Modified: 2019-11-17 14:51:55
# Description:	1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
# Description:	2. Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
# Description:	3. 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
#########################################################################

from functools import reduce

def normalize(name):
    name = name.capitalize()
    return name
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x, y: x * y, L)
#测试：
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

def str2float(s):
    ls = s.split('.')
    a = reduce(lambda x,y: x * 10 + y,map(float,ls[0]))
    b = reduce(lambda x,y: x * 10 + y,map(float,ls[1]))
    f = a + b/(10**len(ls[1]))
    return f
#测试：
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

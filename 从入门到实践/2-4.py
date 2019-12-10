#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: 2-4.py
# Created on : 2019-11-21 17:04:14
# Author: cogito0823
# Last Modified: 2019-11-21 17:04:14
# Description: 调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
#########################################################################

name = input('Username: ')
def printname(name):
    print(name)
printname(name.lower())
printname(name.upper())
printname(name.title())

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: 2-7.py
# Created on : 2019-11-21 17:57:52
# Author: cogito0823
# Last Modified: 2019-11-21 17:57:52
# Description: 剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
# Description：打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。
#########################################################################


name = '\t\n\t\nsdfsdfsadfsdfsdfdf\n\t\n\t'
print('%s\n%s\n%s' % (name.lstrip(),name.rstrip(),name.strip()))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: 2-5.py
# Created on : 2019-11-21 17:12:17
# Author: cogito0823
# Last Modified: 2019-11-21 17:12:17
# Description: 名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号)
# ：
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
#########################################################################

name = input('Personality: ').title()
saying = input('Sying: ')
print('%s once said, "%s"' % (name , saying))

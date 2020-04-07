#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: multiprocess.py
# Created on : 2020-04-07 23:03:06
# Author: cogito0823
# Last Modified: 2020-04-07 23:03:06
# Description:
#########################################################################

import os

print(f'{os.getpid()}')

pid = os.fork()

if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

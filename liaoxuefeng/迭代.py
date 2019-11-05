#!/usr/bin/env python
# -*- coding: utf-8  -*-
def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    maxNum = L[0]
    minNum = L[0]
    for t in (L):
        if t <= minNum:
            minNum = t
        if t >= maxNum:
            maxNum = t
    return (minNum,maxNum)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   bubble_sort.py
@Time    :   2020/03/25 18:05:22
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   None
'''

def bubble_sort(array):
    """冒泡排序
    
    Examples:

    >>> bubble_sort([7,6,5,4,3,2,1,0])
    [0, 1, 2, 3, 4, 5, 6, 7]
    >>> bubble_sort([0, 1, 2, 3, 4, 5, 6, 7])
    [0, 1, 2, 3, 4, 5, 6, 7]
    """
    length = len(array)
    flag = True
    for i in range(length - 1):
        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                flag = False
                array[j], array[j + 1] = array[j + 1], array[j]
        if flag:
            break
    return array
if __name__ == "__main__":
    import doctest
    doctest.testmod()
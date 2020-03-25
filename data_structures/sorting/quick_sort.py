#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   quick_sort.py
@Time    :   2020/03/25 17:40:53
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   None
'''


def quick_sort(array):
    """快排
    
    Examples:
    
    >>> quick_sort([7,6,5,4,3,2,1,0])
    [0, 1, 2, 3, 4, 5, 6, 7]
    """
    
    length = len(array)
    if length <= 1:
        return array
    pivot = array.pop()
    greater, lesser = [], []
    for element in array:
        if element <= pivot:
            lesser.append(element)
        else:
            greater.append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
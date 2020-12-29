#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""sdf.

@File    :   selection_sort.py
@Time    :   2020/03/25 20:31:42
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   None
"""


def selection_sort(array):
    """选择排序.

    Examples:
    >>> selection_sort([7,6,5,4,3,2,1,0])
    [0, 1, 2, 3, 4, 5, 6, 7]
    >>> selection_sort([7,6,5,4,3,2,1])
    [1, 2, 3, 4, 5, 6, 7]

    """
    if not array:
        return array
    length = len(array)
    smallest = 0
    for i in range(length - 1):
        if array[i] > array[i + 1]:
            smallest = i + 1
    array[0], array[smallest] = array[smallest], array[0]
    array[1:] = selection_sort(array[1:])
    return array


if __name__ == "__main__":
    import doctest
    doctest.testmod()

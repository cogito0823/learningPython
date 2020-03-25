#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   heap_sort.py
@Time    :   2020/03/25 18:19:01
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   None
'''

def heapify(array,index,heap_size):
    largest = index
    lchild = index * 2 + 1
    rchild = index * 2 + 2
    if lchild < heap_size and array[lchild] < array[largest]:
        largest = lchild
    if rchild < heap_size and array[rchild] < array[largest]:
        largest = rchild
    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        heapify(array,largest,heap_size)

def heap_sort(array):
    """堆排序
    
    Examples:
    
    >>> heap_sort([7, 6, 5, 4, 3, 2, 1, 0])
    [7, 6, 5, 4, 3, 2, 1, 0]
    >>> heap_sort([0, 1, 2, 3, 4, 5, 6, 7])
    [7, 6, 5, 4, 3, 2, 1, 0]
    >>> heap_sort([1, 2, 3, 4, 5, 6, 7])
    [7, 6, 5, 4, 3, 2, 1]
    >>> heap_sort([])
    []
    >>> heap_sort(None)
    
    """
    if array:
        length = len(array)
        for index in range((length - 1) // 2, -1, -1):
            heapify(array,index,length)
        for i in range(length - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, 0, i)
    return array

if __name__ == "__main__":
    import doctest
    doctest.testmod()
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   binary_heap.py
@Time    :   2020/03/18 11:23:12
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   二叉堆
'''

def up_adjust(array):
    """插入操作"""
    if array: 
        child_index = len(array) - 1
        parent_index = (child_index-1) // 2
        while array[child_index] < array[parent_index] and parent_index >= 0:
            array[child_index], array[parent_index] = array[parent_index], array[child_index]
            child_index = parent_index
            parent_index = (child_index-1) // 2
    return array

def down_adjust(array,parent_index):
    """下调操作"""
    if array:
        lenth = len(array)
        lchild_index = 2 * parent_index + 1
        rchild_index = lchild_index + 1
        while parent_index <= (lenth-1) // 2 and (array[parent_index] > array[lchild_index] or (2 * parent_index + 2 < lenth and array[parent_index] > array[rchild_index])):
            
            if 2 * parent_index + 2 < lenth and array[lchild_index] > array[rchild_index]:
                array[parent_index], array[rchild_index] = array[rchild_index], array[parent_index]
                parent_index = rchild_index
                lchild_index = 2 * parent_index + 1
                rchild_index = lchild_index + 1
            else:
                array[parent_index], array[lchild_index] = array[lchild_index], array[parent_index]
                parent_index = lchild_index
                lchild_index = 2 * parent_index + 1
                rchild_index = lchild_index + 1
    return array

def build_heap(array):
    """生成二叉堆"""
    if array:
        lenth = len(array)
        last_parent_index = (lenth - 2) // 2
        for i in range(last_parent_index + 1):
            parent_index = last_parent_index - i
            down_adjust(array,parent_index)
    return array
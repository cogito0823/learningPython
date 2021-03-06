#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   binary_heap.py
@Time    :   2020/03/18 11:23:12
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   二叉堆 其特殊情况可以构建优先队列，即插入元素 + 删去根元素
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
        if lenth == 1:
            return array
        lchild_index = 2 * parent_index + 1
        rchild_index = lchild_index + 1
        while (parent_index <= (lenth-2) // 2 and
               (array[parent_index] > array[lchild_index] or
                (rchild_index < lenth and array[parent_index] > array[rchild_index]))):
            
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

def delete_element(array):
    if array:
        if len(array) == 1:
            return []
        array[0] = array.pop()
        array = heapify(array,0,len(array))
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

#################### 堆排序 #######################

def heapify(array,index,heap_size):
    largest = index
    lchild_index = 2 * index + 1
    rchild_index = 2 * index + 2
    if lchild_index < heap_size and array[lchild_index] < array[largest]:
        largest = lchild_index
    if rchild_index < heap_size and array[rchild_index] < array[largest]:
        largest = rchild_index
    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        heapify(array,largest,heap_size)
    return array

def heap_sort(array):
    if array:
        array = array[:]
        n = len(array)
        for i in range((n - 1) // 2 , -1, -1):
            array = heapify(array, i, n)
        for i in range(n-1, 0, -1):
            array[0], array[i] = array[i], array[0]
            heapify(array, 0, i)
        return array

#################### 优先队列 ################### 

class Queue(object):
    def __init__(self,array):
        self.array = build_heap(array)
    def insert(self,element):
        self.array.append(element)
        self.array = up_adjust(self.array)
    def pop(self):
        result = self.array[0]
        delete_element(self.array)
        return result
        
        

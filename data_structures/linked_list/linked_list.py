#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   find_repeat_number.py
@Time    :   2021/02/03 00:35:32
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   链表类
'''


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    """通过 node 对象，创建一个链表类
    
    Examples:

    >>> link = LinkedList()
    >>> link.insert(0, 0)
    >>> link.insert(1, 1)
    >>> link.insert(3, 3)
    Traceback (most recent call last):
    Exception: 越界
    >>> link.insert(2, 2)
    >>> link.insert(3, 3)
    >>> link.get(1).data
    1
    >>> link.get(2).data
    2
    >>> link.remove(3) #doctest: +ELLIPSIS
    <__main__.Node object at 0x...>
    >>> link.get(3)
    Traceback (most recent call last):
      File "/root/anaconda3/lib/python3.7/doctest.py", line 1329, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.LinkedList[9]>", line 1, in <module>
        link.get(3).data
      File "linded_list.py", line 54, in get
        raise Exception("越界")
    Exception: 越界 
    """

    def __init__(self): 
        self.size = 0 
        self.head = None 
        self.tail = None 
    
    def get(self, index): 
        if index < 0 or index >= self.size: 
            raise Exception("越界") 
        node = self.head 
        for _ in range(index): 
            node = node.next 
        return node 
    
    def set(self, index, value): 
        node = self.get(index) 
        node.data = value 
    
    def insert(self, index, value): 
        if index < 0 or index > self.size:  
            raise Exception("越界") 
        node = Node(value) 
        # 空链表 
        if self.size == 0: 
            self.head = node 
            self.tail = node 
        # 头部插入 
        elif index == 0: 
            self.head = node 
            self.next = node 
        # 尾部插入
        elif index == self.size: 
            self.tail.next = node 
            self.tail = node 
        else: 
            front_node = self.get(index - 1) 
            next_node = self.get(index) 
            front_node.next = node 
            node.next = next_node 
        self.size += 1 
    
    def remove(self, index): 
        if index < 0 or index >= self.size: 
            raise Exception("越界") 
        # 头部删除 
        if index == 0: 
            removed_node = self.head 
            self.head = self.head.next 
        # 尾部删除 
        elif index == self.size - 1: 
            removed_node = self.tail 
            self.tail = self.get(index - 1) 
            self.tail.next = None 
        else: 
            removed_node = self.get(index) 
            front_node = self.get(index-1) 
            next_node = self.get(index+1) 
            front_node.next = next_node 
        self.size -= 1 
        return removed_node


if __name__ == "__main__":
    import doctest
    doctest.testmod()

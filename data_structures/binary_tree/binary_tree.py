#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   binary_tree.py
@Time    :   2020/03/17 11:40:06
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   递归生成二叉树、遍历二叉树（层次遍历使用队列）
'''

import queue

class Node():
    """节点类"""
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.data)
    __str__ = __repr__
    def __eq__(self,other):
        """重构__eq__方法"""
        return (self.__class__ == other.__class__ and 
                self.data == other.data and 
                ((not self.left_child and not other.left_child) or self.left_child.data == other.left_child.data) and 
                ((not self.right_child and not other.right_child) or self.right_child.data == other.right_child.data))

        
def create_binary_tree(array):
    if array:
        data = array.pop(0)
        if data is not None:
            node = Node(data)
            node.left = create_binary_tree(array)
            node.right = create_binary_tree(array)
            return node
    return None
def pre_order_traveral(node):
    if node:
        print(node.data)
        pre_order_traveral(node.left)
        pre_order_traveral(node.right)
def in_order_traveral(node):
    if node:
        in_order_traveral(node.left)
        print(node.data)
        in_order_traveral(node.right)
def post_order_traveral(node):
    if node:
        post_order_traveral(node.left)
        post_order_traveral(node.right)
        print(node.data)
def pre_order_traveral_via_stack(root):
    if root:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                print(node)
                stack.append(node.right)
                stack.append(node.left)
def level_order_traveral(root):
    if root:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                print(node)
                queue.append(node.left)
                queue.append(node.right)

if __name__ == "__main__":
    node = create_binary_tree([1,0,2,3,4,None,None,5,None,None,6,None,None,None,None])
    pre_order_traveral(node)
    level_order_traveral(node)
    node = create_binary_tree([1,2,4, 8, None, None, 9, None, None, 5, None, None, 3, 6, None, None, 7])
    pre_order_traveral(node)
    level_order_traveral(node)

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
    
    def __eq__(self,other):
        """重构__eq__方法"""
        return (self.__class__ == other.__class__ and 
                self.data == other.data and 
                ((not self.left_child and not other.left_child) or self.left_child.data == other.left_child.data) and 
                ((not self.right_child and not other.right_child) or self.right_child.data == other.right_child.data))

        
def create_binary_tree(tree_list):
    """通过一个数组创建二叉树"""
    if tree_list:
        data = tree_list.pop(0)
        if data:
            node = Node(data)
            node.left_child = create_binary_tree(tree_list)
            node.right_child = create_binary_tree(tree_list)
            return node
    return None

def pre_order_traversal(node):
    """先序遍历"""
    result = []
    def traversal(node):
        if node:
            result.append(node.data)
            traversal(node.left_child)
            traversal(node.right_child)
    traversal(node)
    return result

def in_order_traversal(node):
    """中序遍历"""
    result = []
    # 迭代算法
    def traversal(node):
        if node:
            traversal(node.left_child)
            result.append(node.data)
            traversal(node.right_child)
    traversal(node)
    return result    

def post_order_traversal(node):
    """后序遍历"""
    result = []
    def traversal(node):
        if node:
            traversal(node.left_child)
            traversal(node.right_child)
            result.append(node.data)
    traversal(node)
    return result

def level_order_traversal(node):
    """层序遍历"""
    result = []
    tree_queue = queue.Queue()
    tree_queue.put(node)
    while not tree_queue.empty() and node:
        node = tree_queue.get()
        result.append(node.data)
        if node.left_child:
            tree_queue.put(node.left_child)
        if node.right_child:
            tree_queue.put(node.right_child)
    return result

if __name__ == "__main__":
    node = create_binary_tree([1,2,3,4,None,None,5,None,None,6,None,None,None,None])
    List = level_order_traversal(node)
    for i in List:
        print(i)
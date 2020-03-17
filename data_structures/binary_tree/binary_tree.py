#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   binary_tree.py
@Time    :   2020/03/17 11:40:06
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   生成二叉树、遍历二叉树
'''

class Node():
    """节点类"""
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
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

def pre_order_Traveral(node):
    """先序遍历"""
    result = []
    if node:
        result.append(node.data)
        pre_order_Traveral(node.left_child)
        pre_order_Traveral(node.right_child)
    return result
   
def in_order_Traveral(node):
    """中序遍历"""
    result = []
    if node:
        in_order_Traveral(node.left_child)
        result.append(node.data)
        in_order_Traveral(node.right_child)
        
def post_order_Traveral(node):
    """后序遍历"""
    result = []
    if node:
        post_order_Traveral(node.left_child)
        post_order_Traveral(node.right_child)
        result.append(node.data)

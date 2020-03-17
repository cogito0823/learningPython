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
    
    def __eq__(self,other):
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

def pre_order_traveral(node):
    """先序遍历"""
    result = []
    def traveral(node):
        if node:
            result.append(node.data)
            traveral(node.left_child)
            traveral(node.right_child)
    traveral(node)
    return result

def in_order_traveral(node):
    """中序遍历"""
    result = []
    # 迭代算法
    def traveral(node):
        if node:
            traveral(node.left_child)
            result.append(node.data)
            traveral(node.right_child)
    traveral(node)
    return result    

def post_order_traveral(node):
    """后序遍历"""
    result = []
    def traveral(node):
        if node:
            traveral(node.left_child)
            traveral(node.right_child)
            result.append(node.data)
    traveral(node)
    return result

if __name__ == "__main__":
    node = create_binary_tree([1,2,3,4,None,None,5,None,None,6,None,None,None,None])
    List = post_order_traveral(node)
    for i in List:
        print(i)
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   stack_binary_tree.py
@Time    :   2020/03/16 23:15:26
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   用栈遍历二叉树
'''

class Node():
    """节点类"""
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None
    """重构__wq__方法"""
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
        
def pre_order_traversal(node):
    """先序遍历"""
    result = []
    tree_stack = []
    while node or tree_stack:
        while node:
            result.append(node.data)
            tree_stack.append(node)
            node = node.left_child
        
        if tree_stack:
            node = tree_stack.pop()
            node = node.right_child
    return result

def in_order_traversal(node):
    """中序遍历"""
    result = []
    tree_stack = []
    while node or tree_stack:
        while node:
            tree_stack.append(node)
            node = node.left_child
        
        if tree_stack:
            node = tree_stack.pop()
            if node:
                result.append(node.data)
            node = node.right_child
    return result

# def post_order_traversal(node):
#     """后序遍历"""
#     # result = []
#     tree_stack = [node]
#     while tree_stack:
#         while node:
#             while node.left_child:
#                 tree_stack.append(node.left_child)
#                 node = node.left_child
#             node = tree_stack[-1]
        
#         if node.right_child:
#             node = node.right_child
#         else:
#             print(node.data)
#             node = tree_stack.pop()
#             node = tree_stack[-1].right_child
#             tree_stack.append(node)
    
if __name__ == "__main__":
    pre_order_traversal(create_binary_tree([1,2,3,4,None,None,5,None,None,6,None,None,None]))

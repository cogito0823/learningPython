#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: test_binary_tree.py
# Created on : 2020-03-14 12:14:28
# Author: cogito0823
# Last Modified: 2020-03-14 12:14:28
# Description:
#########################################################################

import unittest
import stack_binary_tree as bt

class BinaryTreeTestCase(unittest.TestCase):
    """测试binary_tree.py"""
    def setUp(self):
        self.node = bt.Node(1)
        self.node.left_child = bt.Node(2)
        self.node.right_child = None
        self.node_None = bt.create_binary_tree(None)
        self.node_None1 = bt.create_binary_tree([None])
        self.node_full = bt.create_binary_tree([1,2,3,4,None,None,5,None,None,6,None,None,None,None])
        
    def test_create_tree(self):
        """能够正确生成二叉树吗？"""
        self.assertEqual(self.node_None,None)
        self.assertEqual(self.node_None1,None)
        self.assertTrue(self.node_full == self.node)
    
    def test_pre_order_traveral(self):
        # 当二叉树不为空
        result = bt.pre_order_traveral(self.node_full)
        self.assertListEqual(result,[1,2,3,4,5,6])
        
        # 当二叉树为空
        result_None = bt.pre_order_traveral(None)
        self.assertListEqual(result_None,[])
        
    # def test_in_order_traveral(self):
    #     result = bt.pre_order_traveral(self.node_full)
    #     self.assertListEqual(result,[1,2,3,4,5,6])
        
    #     result_None = bt.pre_order_traveral(None)
    #     self.assertListEqual(result_None,[])
    
    
unittest.main()
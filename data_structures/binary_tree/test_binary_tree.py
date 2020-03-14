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
import binary_tree as bt

class BinaryTreeTestCase(unittest.TestCase):
    """测试binary_tree.py"""

    def test_create_tree(self):
        """能够正确生成二叉树吗？"""
        node = bt.Node(1)
        node.left_child = 2
        node.right_child = None
        node_full = bt.create_binary_tree([1,2,3,None,None,None,None])
        
        
        node_None = bt.create_binary_tree(None)
        self.assertEqual(node_None,None)
        
        node_None1 = bt.create_binary_tree([None])
        self.assertEqual(node_None1,None)
        
        self.assertEqual(node_full.data,node.data)
        self.assertEqual(node_full.left_child.data,2)
        self.assertEqual(node_full.right_child,None)

unittest.main()
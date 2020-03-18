#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   test_binary_heap.py
@Time    :   2020/03/18 11:57:06
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   测试二叉堆
'''

import binary_heap as binary_heap
import unittest

class BheapTestCase(unittest.TestCase):
    """测试二叉堆"""
    
    def setUp(self):
        """setIp"""
        self.array_full = [0,1,2,3,4,5,6,7]
        self.array_up = [1,2,3,4,5,6,7,0]
        self.array_down = [7,0,1,2,3,4,5,6]
        self.array_build = [4,3,7,0,2,6,5,1]
        self.array_emp = []
        self.array_None = None
    def test_up_adjust(self):
        """测试插入操作"""
        result_up = binary_heap.up_adjust(self.array_up)
        result_emp = binary_heap.up_adjust(self.array_emp)
        result_None = binary_heap.up_adjust(self.array_None)
        
        self.assertListEqual(result_up,[0,1,3,2,5,6,7,4])
        self.assertEqual(result_emp,[])
        self.assertEqual(result_None,None)
    def test_down_adjust(self):
        """测试下调操作"""
        result_down = binary_heap.down_adjust(self.array_down,0)
        result_emp = binary_heap.down_adjust(self.array_emp,0)
        result_None = binary_heap.down_adjust(self.array_None,0)
        
        self.assertListEqual(result_down,[0,2,1,6,3,4,5,7])
        self.assertEqual(result_emp,[])
        self.assertEqual(result_None,None)
    def test_build_heap(self):
        """测试生成二叉堆操作"""
        result_build = binary_heap.build_heap(self.array_build)
        result_emp = binary_heap.build_heap(self.array_emp)
        result_None = binary_heap.build_heap(self.array_None)
        
        self.assertListEqual(result_build,[0,1,5,3,2,6,7,4])
        self.assertEqual(result_emp,[])
        self.assertEqual(result_None,None)  
        
if __name__ == "__main__":
    unittest.main()
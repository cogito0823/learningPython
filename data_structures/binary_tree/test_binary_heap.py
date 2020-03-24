#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File    :   test_binary_heap.py
@Time    :   2020/03/18 11:57:06
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   测试二叉堆 优先队列
'''

import binary_heap as binary_heap
import unittest

class BheapTestCase(unittest.TestCase):
    """测试二叉堆"""
    
    def setUp(self):
        """setIp"""
        # [0,1,2,3,4,5,6,7] = [0,1,2,3,4,5,6,7]
        # [0,1,2,3,4,5,6] = [0,1,2,3,4,5,6]
        # [1,2,3,4,5,6,7,0] = [1,2,3,4,5,6,7,0]
        # [1,2,3,4,5,6,0] = [1,2,3,4,5,6,0]
        # [7,0,1,2,3,4,5,6] = [7,0,1,2,3,4,5,6]
        # [7,1,2,3,4,5,6] = [7,1,2,3,4,5,6]
        # [4,3,7,0,2,6,5,1] = [4,3,7,0,2,6,5,1]
        # [1] = [1]
        # [] = []
        # None = None
    def test_up_adjust(self):
        """测试插入操作"""
        result_up1 = binary_heap.up_adjust([1,2,3,4,5,6,7,0])
        result_up2 = binary_heap.up_adjust([1,2,3,4,5,6,0])
        result_one_element = binary_heap.up_adjust([1])
        result_emp = binary_heap.up_adjust([])
        result_None = binary_heap.up_adjust(None)
        
        self.assertListEqual(result_up1,[0,1,3,2,5,6,7,4])
        self.assertListEqual(result_up2,[0,2,1,4,5,6,3])
        self.assertListEqual(result_one_element,[1])
        self.assertEqual(result_emp,[])
        self.assertEqual(result_None,None)
    def test_down_adjust(self):
        """测试下调操作"""
        result_down1 = binary_heap.down_adjust([7,0,1,2,3,4,5,6],0)
        result_down2 = binary_heap.down_adjust([7,1,2,3,4,5,6],0)
        result_one_element = binary_heap.down_adjust([1],0)
        result_emp = binary_heap.down_adjust([],0)
        result_None = binary_heap.down_adjust(None,0)
        
        self.assertListEqual(result_down1,[0, 2, 1, 6, 3, 4, 5, 7])
        self.assertListEqual(result_down2,[1,3,2,7,4,5,6])
        self.assertListEqual(result_one_element,[1])
        self.assertEqual(result_emp,[])
        self.assertEqual(result_None,None)
    def test_build_heap(self):
        """测试生成二叉堆操作"""
        result_build = binary_heap.build_heap([4,3,7,0,2,6,5,1])
        result_one_element = binary_heap.build_heap([1])
        result_emp = binary_heap.build_heap([])
        result_None = binary_heap.build_heap(None)
        
        self.assertListEqual(result_build,[0,1,5,3,2,6,7,4])
        self.assertListEqual(result_one_element,[1])
        self.assertEqual(result_emp,[])
        self.assertEqual(result_None,None)  
    def test_delete_element(self):
        """测试删除根节点"""
        result_delete_element1 = binary_heap.delete_element([0,1,2,3,4,5,6,7])
        result_delete_element2 = binary_heap.delete_element([0,1,2,3,4,5,6])
        result_one_element = binary_heap.delete_element([1])
        result_emp = binary_heap.delete_element([])
        result_None = binary_heap.delete_element(None)
        
        self.assertListEqual(result_delete_element1,[1,3,2,7,4,5,6])
        self.assertListEqual(result_delete_element2,[1,3,2,6,4,5])
        self.assertListEqual(result_one_element,[])
        self.assertEqual(result_emp,[])
        self.assertEqual(result_None,None)
        
    def test_queue(self):
        """测试优先队列"""
        array = [5,6,2,3,4,0,1]
        queue = binary_heap.Queue(array)
        queue_array = queue.array.copy()
        pop = queue.pop()
        self.assertListEqual(queue_array,[0,3,1,6,4,2,5])
        self.assertListEqual(queue.array,[1,3,2,6,4,5])
        self.assertEqual(pop,0)
    
    def test_heap_sort(self):
        sort_result = binary_heap.heap_sort(list([0,1,2,3,4,5,6,7]))
        self.assertListEqual(sort_result,list([7,6,5,4,3,2,1,0]))
            
if __name__ == "__main__":
    unittest.main()
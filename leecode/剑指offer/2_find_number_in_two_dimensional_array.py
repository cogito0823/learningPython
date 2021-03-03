#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   2_find_number_from_two_dimensional_array.py
@Time    :   2021/02/15 17:36:58
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   二维数组中的查找
'''

from typing import List


class Solution:
    """二维数组中的查找
    
    在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

    示例:
    现有矩阵 matrix 如下：
    [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
    给定 target = 5，返回 true。
    给定 target = 20，返回 false。

    限制：
    0 <= n <= 1000
    0 <= m <= 1000
    """

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int):
        """[summary]

        Args:
            matrix (List[List[int]]): [description]
            target (int): [description]

        examples:
        >>> Solution().findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
        True
        >>> Solution().findNumberIn2DArray([], 0)
        False
        """
        if not matrix:
            return False
        column_index = Solution.binarySearch(nums=matrix[0], start_index=0, end_index=len(matrix[0]) - 1, target_number=target)

        if column_index == -1:
            return False

        column_nums = [array[column_index] for array in matrix]

        row_index = Solution.binarySearch(nums=column_nums, start_index=0, end_index=len(column_nums) - 1, target_number=target)

        if matrix[row_index][column_index] == target:
            return True
        else:
            return False


    def binarySearch(nums: List[int], start_index: int, end_index: int, target_number: int):
        """二分查找最小相邻数字, 返回该数字在数组中的索引值

        Args:
            nums (list): 数组
            start_index (int): 起始索引值
            end_index (int): 终止索引值
            target_number (int): 目标数字

        Returns:
            index_value (int): 最小相邻数字在数组中的索引值

        examples:
        >>> Solution.binarySearch([1,4,7,11,15], 0, 4, 5)
        1
        >>> Solution.binarySearch([], 0, -1, 5)
        -1
        >>> Solution.binarySearch([1,2], 0, 1, 1)
        0
        >>> Solution.binarySearch([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        """
        
        target_index = -1

        if nums:

            if end_index == start_index:
                target_index = end_index

            elif end_index > start_index:

                length = end_index - start_index + 1
                mid = start_index + (end_index - start_index) // 2

                if start_index + 1 == end_index:
                    if target_number >= nums[end_index]:
                        target_index = end_index
                    elif target_number >= nums[start_index]:
                        target_index = start_index

                else:
                    if nums[mid] == target_number:
                        target_index = mid
                    
                    elif nums[mid] > target_number:
                        target_index = Solution.binarySearch(nums, start_index, mid-1, target_number)

                    else:
                       target_index = Solution.binarySearch(nums, mid, end_index, target_number)

        return target_index


if __name__ == '__main__':
    import doctest
    doctest.testmod()

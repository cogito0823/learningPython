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
        if not matrix or not matrix[0]:
            return False
        len_row = len(matrix)
        len_col = len(matrix[0])
        i, j = 0, len_col-1
        while i < len_row and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j -= 1
            else:
                i += 1
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()

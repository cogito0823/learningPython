#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   find_repeat_number.py
@Time    :   2021/02/03 00:35:32
@Author  :   cogito0823
@Contact :   754032908@qq.com
@Desc    :   数组中的重复数字
'''

from typing import List


class Solution:
    """在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

    示例 1：

    输入：
    [2, 3, 1, 0, 2, 5, 3]
    输出：2 或 3
    """

    def findRepeatNumberBySort(self, nums: List[int]):
        """使用 list 的 sort 方法对数组进行排序，然后找出重复数字

        Args:
            nums (List[int]): [description]

        Returns:
            repeat (int): 重复的数字

        Examples:

        >>> Solution().findRepeatNumberBySort([2, 3, 1, 0, 2, 5, 3])
        2
        """
        repeat = -1
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return repeat

    def findRepeatNumberBySet(self, nums: List[int]):
        """使用 set 找出重复数字

        Args:
            nums (List[int]): [description]

        Returns:
            repeat (int): 重复的数字

        Examples:

        >>> Solution().findRepeatNumberBySet([2, 3, 1, 0, 2, 5, 3])
        2
        """
        repeat = -1
        temp_set = set([])
        for i in range(len(nums)):
            temp_set.add(nums[i])
            if len(temp_set) == i:
                return nums[i]
        return repeat


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
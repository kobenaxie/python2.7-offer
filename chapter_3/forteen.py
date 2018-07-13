# -*- coding:utf-8 -*-
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分.
思路：用头尾两个指针。头指针用来找到左侧的偶数，尾指针用来找到右侧的奇数，知道头尾指针相遇。
"""
class Solution:
    def reOrderArray(self, array):
        # write code here
        if array is None or len(array)==0:
            return None
        p_start = 0
        p_end = len(array)-1
        while (p_start<p_end):
            # --->>> forward find even
            while (p_start<p_end) and (array[p_start]&1 != 0):
                p_start += 1
            # <<<--- backward find odd
            while (p_start<p_end) and array[p_end]&1 == 0:
                p_end -= 1
            # swap odd and even
            if p_start < p_end:
                tmp = array[p_start]
                array[p_start] = array[p_end]
                array[p_end] = tmp

        return array

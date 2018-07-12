# coding:utf-8
import random
"""
快排：
1. 找到一个基准pivot
2. 将数组中小于pivot的数移动到pivot, 将大于pivot的数移动到右边，以pivot为分界，这一步叫分区: partition
3. 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序
"""

def swap_list(array, start, end):
    assert 0<=start<=len(array) and 0<=end<=len(array)
    tmp = array[start]
    array[start] = array[end]
    array[end] = tmp
    del tmp
    return array

class Solution(object):
    def partition(self, array, start, end):
        """
        end < len(array)
        return the pivot position index
        """
        # spacial case
        if start<0 or end>=len(array) or array==None:
            import sys
            sys.exit('Invalid parameters')

        # 1. random set a pivot
        index = random.randint(start, end) # return close partition of [start, end]
        pivot = array[index]
        # 2. partition
        small = start - 1 #positon inedx of current number that less than pivot=array[index]
        array = swap_list(array, index, end) # put pivot at end
        for index in range(start, end+1):
            if array[index] < pivot:
                small += 1
                if small != index: # make not resorce waste
                    array = swap_list(array, small, index)
        # put pivot at middle of sub_arrays
        small += 1
        array = swap_list(array, small, end)
        return small

    def quick_sort(self, array, start, end):
        if start==end:
            return array
        # 3. recursively sort sub arrays
        pivot_index = self.partition(array, start, end)
        if pivot_index > start:
            self.quick_sort(array, start, pivot_index - 1)
        if pivot_index < end:
            self.quick_sort(array, pivot_index + 1, end)
        print array

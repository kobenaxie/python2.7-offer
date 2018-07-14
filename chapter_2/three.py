# coding:utf-8
"""
问题描述：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
          请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
思路：从第一行的最后一列开始查找，如果该数大于目标值，说明最后一列的所有值都大于目标，因此列索引减一；
                               若果该书小于目标值，说明第一行的所有值都小于目标，因此行索引加一：
"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        num_rows = len(array)
        num_colums = len(array[0])
        row = 0
        col = num_colums - 1
        while row<num_rows and col>=0:
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

# coding:utf-8
"""
问题描述：用一条语句判断一个整数是不是2的整数次方。
思路：一个整数如果是2的整数次方，说明该整数中有且仅含一个1，其余位均为0，因此可以用该整数与其减一进行按位与，这样就可以把唯一的1变为0.

问题描述：输入两个整数m和n，计算需要改变m的二进制表示中的多少位才能得到n.
思路：分两步：1）m和n异或；2）统计异或结果中1的个数。
"""
class Solution(object):
    def is_pow_two(self, n):
        if n & (n-1) == 0:
            return True
        else:
            return False
    def steps_m_to_n(self, m, n):
        m_n = m ^ n
        return self.NumberOf1(m_n)

    def NumberOf1(self, n):
        """最优：将n与n-1按位与，会将n的二进制表示中的最右边一个1变为0"""
        count = 0
        # 如果n为负数，n-1只会越来越小，不会为0，因此不能用while n！=0作为循环条件:
        while n&0xffffffff != 0:
            count += 1
            n = n & n-1
        return count

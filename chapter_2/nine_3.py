# -*- coding:utf-8 -*-
"""
问题描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
思路：
n=1, f(1) = 1
n=2, f(2) = f(首次跳一个台阶) + 首次跳n个台阶 = f(1) + 1 = 2*f(1)
n=3, f(3) = f(首次跳一个台阶) + f(首次跳两个台阶) +　首次跳n个台阶 = f(2) + f(1) + 1 = f(2) + f(2) = 2*f(2)
n=4以此类推
f(n) = 2*f(n-1)
"""
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number<=0:
            return False
        if number==1:
            return 1
        elif number==2:
            return 2
        else:
            fib_minus_one = 2
            fib = 0
            for _ in range(2, number):
                fib = 2*fib_minus_one
                fib_minus_one = fib
            return fib

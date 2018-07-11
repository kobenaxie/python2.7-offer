# coding: utf-8
"""
问题描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级台阶总共有多少种跳法。
思路：
n=1: f(1) = 1
n=2: f(2) = 2
n=3: 分成两种情况，第一个步跳一个台阶，剩下两个台阶共有f(2)种方法；第一步跳2个台阶，剩下1个台阶共有f(1)总方法，
      因此，f(3) = f(2) + f(1)
以此类推。。。
"""
class solution():
    def how_many_methods(n):
        if n<=0:
            return False
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            methods_minus_two = 1
            methods_minus_one = 2
            methods = 0
            for _ in range(2, n):
                methods = methods_minus_one + methods_minus_two
                methods_minus_two = methods_minus_one
                methods_minus_one = methods
            return methods

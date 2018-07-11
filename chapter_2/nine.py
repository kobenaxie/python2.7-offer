# -*- coding:utf-8 -*-
"""
斐波那契数列
f(0) = 0
f(1) = 1
f(n) = f(n-1) + f(n-2) n>=2时
之所以没有使用递归，是因为递归的过程中会产生很多的重复计算，如：
f(9) = f(8)+f(7)
f(8) = f(7)+f(6)
在计算f(8)和f(9)的过程中都会计算f(7),造成重复计算。
""" 
class Solution:
    def Fibonacci(self, n):
        # write code here
        # fib = fib_minus_one + fib_minus_two
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            fib_minus_two, fib_minus_one = 0, 1
            fib = 0
            for i in xrange(1, n):
                fib = fib_minus_one + fib_minus_two
                fib_minus_two = fib_minus_one
                fib_minus_one = fib
            return fib

# -*- coding:utf-8 -*-
"""
问题描述：
思路：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
n=1, 小矩形只能竖着放，f(1) = 1
n=2, 1）第一个小矩形竖着放，第二个小矩形也只能竖着放，共f(1)种；2）第一个小矩形横着放，第二个也只能横着放，一种。f(2)=f(1)+1
n=3, 1)第一个小矩形竖着放，剩下的两个小矩形有f(2)中放法；2）第一个小矩形横着放，剩下的两个小矩形只能一个横着放一个竖着放f(1)。f(3)=f(2)+f(1)
n=4, 以此类推
f(n) = f(n-1)+f(n-2), n>2时
"""
class Solution:
    def rectCover(self, number):
        # write code here
        if number<=0:
            return False
        elif number==1:
            return 1
        elif number==2:
            return 2
        else:
            fib = 0
            fib_minus_two = 1
            fib_minus_one = 2
            for _ in range(2, number):
                fib  = fib_minus_one + fib_minus_two
                fib_minus_two = fib_minus_one
                fib_minus_one = fib
            return fib

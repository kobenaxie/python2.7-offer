# -*- coding:utf-8 -*-
"""
问题描述：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
思路1：整数n和1进行与运算相当于n的最后一位和1与运算，依次将n右移一位并与1按位与即可，统计与的结果为1的次数。
      但是如果n为负数，n右移一位会在首位补1，因此会导致无限循环。
思路2：保持n不动，将1左移n的二进制位长度，统计与的结果中不为0的个数。【问题是怎样知道n的二进制表示的长度，不然1一直左移不会变为0，
      会变成很小的负数】
思路3：1）如果一个整数不为0，那么这个整数至少有一位是1。如果我们把这个整数减1，那么原来处在整数最右边的1就会变为0，
         原来在1后面的所有的0都会变成1(如果最右边的1后面还有0的话)。其余所有位将不会受到影响。
       2）把原来的整数和减去1之后的结果做与运算，从原来整数最右边一个1那一位开始所有位都会变成0。
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        return NumberOf1_method_2(n)

# ref: https://blog.csdn.net/u010005281/article/details/79851154
def NumberOf1_method_1(n):
    """n右移一位后和1做与运算， 但是n为负数的时候会死循环"""
    count = 0
    while n:
        if n & 1:
            count += 1
        n = n >> 1
    return count

def NumberOf1_method_2(n):
    """常规：1左移一位后与n按位与，与的结果为1表示该位为1"""
    one = 1
    count = 0
    while one:
        if one & n:
            count += 1
        one = one << 1
        # 一直右移会导致无限长二进制（长整型无限长），one会变成很小的负数，循环不会停止
        if one > 0x80000000:
            break
        
    return count

def NumberOf1_method_3(n):
    """最优：将n与n-1按位与，会将n的二进制表示中的最右边一个1变为0"""
    count = 0
    # 如果n为负数，n-1只会越来越小，不会为0，因此不能用while n！=0作为循环条件:
    while n&0xffffffff != 0:
        count += 1
        n = n & n-1
    return count

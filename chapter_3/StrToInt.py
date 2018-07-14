# -*- coding:utf-8 -*-
"""
问题描述：将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
         要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
python不支持C的字符串相减得到整数的功能，需要借助ord(string)函数
思路：如果字符串长度为1，有可能是'+', '-', '0123456789'因此需要特殊处理
如果字符串长度大于1，而且首字符为'-'的时候，在最后的结果需要去负数，即0-n
"""
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        # length == 1
        if len(s)==1:
            if s not in '0123456789':
                return 0
            else:
                return ord(s) - ord('0')
        # length > 1
        if s[0] == '+':
            return str2num(s[1:])
        elif s[0] == '-':
            return 0 - str2num(s[1:])
        else:
            return str2num(s)
        
def str2num(s):
    n = 0
    for c in s:
        if c not in '0123456789':
            return 0
        else:
            n = 10*n
            n = n + (ord(c) - ord('0'))
    return n

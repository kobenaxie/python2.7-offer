# -*- coding:utf-8 -*-
"""
问题描述：替换空格， 将空格替换为%20.
这个是作弊？
"""
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        import re
        pattern = re.compile(' ')
        res = re.sub(pattern, '%20', s)
        return res

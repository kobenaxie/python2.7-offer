# -*- coding:utf-8 -*-
"""
问题描述：输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
主要问题是Python如何定义链表、节点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        res = []
        while stack:
            res.append(stack.pop())
        return res

# 实例化链表头
testListNode = ListNode(58)
testListNode.next = ListNode(24)
testListNode.next.next = ListNode(0)
testListNode.next.next.next = ListNode(67)

s = Solution()
print s.printListFromTailToHead(testListNode)

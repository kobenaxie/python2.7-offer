# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        # 向栈1添加节点
        self.stack1.insert(0, node)
    def pop(self):
        # 如果栈2空，将栈1内节点移动到栈2内
        if len(self.stack2)==0:
            if len(self.stack1)==0:
                return None
            else:
                for _ in range(len(self.stack1)):
                    self.stack2.insert(0, self.stack1.pop())
                return self.stack2.pop()
        else:
            return self.stack2.pop()

# coding:utf-8
"""
两个队列实现栈
思路：queue1用于入栈及出栈；queue2用于出栈过程中保存queue1中的元素。
    入栈：入队queue1即可。
    出栈：当queue1中只含有一个元素时，直接pop即可；当queue1中元素多余一个时，
          将queue1中元素逐个出队并入队到queue2，直至queue1中只含有一个元素，pop即可。
"""
class solution():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        
    def push(self, node):
        """
        [node1, node0] --> [node, node1, node0]
        """
        self.insert(0, node)
        
    def pop(self):
        """queue1 = []"""
        if len(self.queue1)==0:
            return None
        """queue1 = [node]"""
        elif len(self.queue1)==1:
            self.queue1.pop()
        """queue1 = [node3, node2, node1, node0]"""
        else:
            for _ in range(len(self.queue1)-1):
                self.queue2.insert(-1, self.queue1.pop())
            out = self.queue1.pop()
            self.queue1, self.queue2 = self.queue2, []
            return out
            

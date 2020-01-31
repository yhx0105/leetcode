'''用两个栈来实现一个队列，完成队列的Push和Pop操作。
队列中的元素为int类型。'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]

    def push(self, node):
        # write code here
        self.stackA.append(node)


    def pop(self):
        # return xx
        if not len(self.stackB)==0:
            return self.stackB.pop()
        else:
            while len(self.stackA)>0:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    #方法1 从头读取，反向输出
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        l=[]
        while listNode:
            l.append(listNode.val)
            listNode=listNode.next
        l.reverse()
        return l

if __name__ == '__main__':
    x=[67,0,24,58]
    l1=ListNode(67)
    l2=ListNode(0)
    l3=ListNode(24)
    l4=ListNode(58)
    l1.next=l2
    l2.next=l3
    l3.next=l4
    s=Solution()
    print(s.printListFromTailToHead(l1))

"""
输入一个复杂链表
（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return pHead
        leftpointer=pHead
        #复制节点
        while leftpointer:
            copypointer=RandomListNode(leftpointer.label)
            copypointer.next=leftpointer.next
            leftpointer.next=copypointer
            leftpointer=copypointer.next
        leftpointer=pHead
        #复制random指针
        while leftpointer:
            copypointer=leftpointer.next
            if leftpointer.random:
                copypointer.random=leftpointer.random.next
            leftpointer=leftpointer.next.next
        #拆分
        newHead=pHead.next
        leftpointer=pHead
        while leftpointer:
            copypointer=leftpointer.next
            leftpointer.next=copypointer.next
            if copypointer.next:
                copypointer.next=copypointer.next.next
            else:
                copypointer.next=None
            leftpointer=leftpointer.next
        return newHead

if __name__ == '__main__':
    l1=RandomListNode(1)
    l2=RandomListNode(2)
    l3=RandomListNode(3)
    l4=RandomListNode(4)
    l5=RandomListNode(5)
    l1.next=l2
    l2.next=l3
    l3.next=l4
    l4.next=l5
    s=Solution()
    tmp=s.Clone(l1)
    while tmp:
        print(tmp.label)
        tmp=tmp.next
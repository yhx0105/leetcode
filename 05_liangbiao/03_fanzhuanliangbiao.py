"""
输入一个链表，反转链表后，输出新链表的表头
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList1(self, pHead):
        # write code here
        res=[]
        while pHead:
            res.insert(0,pHead)
            pHead=pHead.next
        for i in range(len(res)-1):
            res[i].next=res[i+1]
        res[len(res)-1].next=None
        return res[0]

    #三指针法,right,mid,left mid指向left,再使得三个指针换位置
    def ReverseList2(self, pHead):
        if pHead==None:
            return None
        if pHead.next==None:
            return pHead
        leftpointer=pHead
        midpointer=leftpointer.next
        rightpointer=midpointer.next

        leftpointer.next=None

        while rightpointer:
            midpointer.next=leftpointer
            leftpointer=midpointer
            midpointer=rightpointer
            rightpointer=rightpointer.next
        midpointer.next=leftpointer
        return midpointer





if __name__ == '__main__':
    p1=ListNode(1)
    p2=ListNode(2)
    p3=ListNode(3)
    p1.next=p2
    p2.next=p3
    s=Solution()
    l1=s.ReverseList2(p1)
    print(l1)

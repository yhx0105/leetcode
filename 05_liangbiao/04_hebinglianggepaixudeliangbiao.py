"""
输入两个单调递增的链表，
输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    #遍历pHead2
    def Merge(self, pHead1, pHead2):
        # write code here
        left1=pHead1
        right1=pHead1.next
        left2=pHead2
        right2=pHead2.next
        while right2:
            while left1.val<=left2.val and right1.val>=left2.val:
                left2 = left1.next
                left2.next=right1
                left2=right2
                right2=right2.next
            left1=right1
            right1=right1.next
        return pHead1

    #递归
    def Merge2(self,pHead1,pHead2):
        if pHead1==None:
            return pHead2
        if pHead2==None:
            return pHead1
        res=None
        if pHead1.val<pHead2.val:
            res=pHead1
            pHead1.next=self.Merge2(pHead1.next,pHead2)
        else:
            res=pHead2
            res.next=self.Merge2(pHead1,pHead2.next)
        return res

    #指针
    def Merge3(self,pHead1,pHead2):
        if pHead1==None:
            return pHead2
        if pHead2==None:
            return pHead1
        pTmp1=pHead1
        pTmp2=pHead2
        if pHead1.val<pHead2.val:
            newHead=pHead1
            pTmp1=pTmp1.next
        else:
            newHead=pHead2
            pTmp2=pTmp2.next
        preHead=newHead

        while pTmp2 and pTmp1:
            if pTmp1.val<pTmp2.val:
                preHead.next=pTmp1
                preHead=pTmp1
                pTmp1=pTmp1.next
            else:
                preHead.next=pTmp2
                preHead=pTmp2
                pTmp2=pTmp2.next
        if pTmp1:
            preHead.next=pTmp1
        else:
            preHead.next=pTmp2
        return newHead


if __name__ == '__main__':
    p11=ListNode(1)
    p12=ListNode(3)
    p13=ListNode(5)
    p11.next=p12
    p12.next=p13
    p21=ListNode(2)
    p22=ListNode(4)
    p23=ListNode(6)
    p21.next=p22
    p22.next=p23
    s=Solution()
    s.Merge3(p11,p21)
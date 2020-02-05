"""
输入两个链表，找出它们的第一个公共结点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    #时间复杂度O(mn)
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pTmp1=pHead1
        pTmp2=pHead2
        while pTmp1:
            while pTmp2:
                if pTmp1==pTmp2:
                    return pTmp2
                else:
                    pTmp2=pTmp2.next
            pTmp1=pTmp1.next
            pTmp2=pHead2
        return None
    #让一个先跳，复杂度为O(n)

    def findEqual(self,pTmp1,pTmp2,k):
        for i in range(k):
            pTmp1 = pTmp1.next
        while pTmp1 != pTmp2:
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next
        return pTmp1

    def FindFirstCommonNode2(self, pHead1, pHead2):
        pTmp1=pHead1
        pTmp2=pHead2
        while pTmp1 and pTmp2:
            pTmp1=pTmp1.next
            pTmp2=pTmp2.next
        if pTmp1:
            count=0
            while pTmp1:
                pTmp1=pTmp1.next
                count+=1
            pTmp1=pHead1
            pTmp2=pHead2
            return self.findEqual(pTmp1,pTmp2,count)
        else:
            count = 0
            while pTmp2:
                pTmp2 = pTmp1.next
                count += 1
            pTmp1 = pHead1
            pTmp2 = pHead2
            return self.findEqual(pTmp2, pTmp1, count)








if __name__ == '__main__':

    l11=ListNode(1)
    l12=ListNode(2)
    l21=ListNode(1)
    l22=ListNode(2)
    l3=ListNode(3)
    l4=ListNode(4)
    l11.next=l12
    l12.next=l3
    l3.next=l4
    l21.next=l22
    l22.next=l3
    s=Solution()
    print(s.FindFirstCommonNode(l11,l21).val)



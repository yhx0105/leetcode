"""
输入一个链表，输出该链表中倒数第k个结点。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #读出来放到，列表里面，完成操作，空间时间复杂度O(n)
    def FindKthToTail1(self, head, k):
        # write code here
        #判断是否为空
        if not head:
            return None
        res=[]
        while head:
            res.insert(0,head)
            head=head.next
        if k>len(res) or k==0:
            return None
        return res[k-1]


    def FindKthToTail2(self, head, k):
        p1=head
        p2=head
        if not p1 or k<=0:
            return None
        while k>1:
            if p2.next!=None:
                p2=p2.next
                k-=1
            else:
                return None
        while p2.next:
            p1=p1.next
            p2=p2.next
        return p1


if __name__ == '__main__':
    l1=ListNode(1)
    l2=ListNode(2)
    l3=ListNode(3)
    l1.next=l2
    l2.next=l3
    s=Solution()
    print(s.FindKthToTail2(l1,1))



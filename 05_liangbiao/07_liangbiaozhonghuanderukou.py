"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，
否则，输出null。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    """遍历一个，再列表里面加一个，如果出项过则返回第一个出现节点，
    若遍历完还没有，返回null,空间复杂度O(n)
    """
    def EntryNodeOfLoop1(self, pHead):
        # write code here
        res=[]
        while pHead:
            res.append(pHead)
            pHead=pHead.next
            if pHead in res:
                return pHead
        return None


    """"
    快慢指针，快指针走2，慢指针走1；如果相遇一定在环里面
    """
    def EntryNodeOfLoop2(self, pHead):
        slow=pHead
        fast=pHead
        if fast.next==None or fast.next.next==None:
            return None
        slow=slow.next
        fast=fast.next.next
        while slow!=fast:
            slow=slow.next
            fast=fast.next.next
            if not fast:
                return None
        slow=pHead
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow

if __name__ == '__main__':
    l1=ListNode(1)
    s=Solution()
    s.EntryNodeOfLoop2(l1)
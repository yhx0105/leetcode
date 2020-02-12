"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印
"""
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        l=[]
        res=[]
        l.append(root)
        while len(l):
            node=l.pop(0)
            res.append(node.val)
            if node.left:
                l.append(node.left)
            if node.right:
                l.append(node.right)
        return res


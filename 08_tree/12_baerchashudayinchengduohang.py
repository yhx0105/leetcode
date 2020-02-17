"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        stack1=[pRoot]
        stack2=[]
        res=[]
        while stack1 or stack2:
            tmplist=[]
            while stack1:
                node=stack1.pop(0)
                tmplist.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            if tmplist:
                res.append(tmplist)
            tmplist=[]
            while stack2:
                node=stack2.pop(0)
                tmplist.append(node)
                if node.left:
                    stack1.append(node.left)
                if node.right:
                    stack1.append(node.right)
            if tmplist:
                res.append(tmplist.val)
        return res
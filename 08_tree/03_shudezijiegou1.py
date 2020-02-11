"""
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1==None  or pRoot2==None:
            return False

        def hasEqual(pRoot1,pRoot2):
            if pRoot2==None:
                return True
            if pRoot1==None:
                return False
            if pRoot1.val==pRoot2.val:
                if pRoot2.left==None:
                    leftEqual=True
                else:
                    leftEqual=hasEqual(pRoot1.left,pRoot2.left)
                if pRoot2.right==None:
                    rightEqual=True
                else:
                    rightEqual=hasEqual(pRoot1.right,pRoot2.right)
                return leftEqual and rightEqual
            return False

        if pRoot1.val==pRoot2.val:
            ret=hasEqual(pRoot1,pRoot2)
            if ret:
                return True

        ret=self.HasSubtree(pRoot1.left,pRoot2)
        if ret:
            return True

        ret=self.HasSubtree(pRoot1.right,pRoot2)
        if ret:
            return True
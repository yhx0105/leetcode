"""
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的
"""
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.compare(pRoot.left,pRoot.right)

    def compare(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val==right.val:
            if self.compare(left.left,right.right) and self.compare(right.left,left.right):
                return True
        return False


if __name__ == '__main__':
    t1=TreeNode(8)
    t2 = TreeNode(6)
    t3 = TreeNode(9)
    t4 = TreeNode(5)
    t5 = TreeNode(7)
    t6 = TreeNode(7)
    t7 = TreeNode(5)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    t3.left=t6
    t3.right=t7

    s=Solution()
    print(s.isSymmetrical(t1))

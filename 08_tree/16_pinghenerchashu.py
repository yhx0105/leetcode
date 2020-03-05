"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #自顶向下递归,缺点：每次都要遍历一遍树
    def isBalanced(self,root):
        if not root:
            return True
        if (abs(self.height(root.left)-self.height(root.right))>1):
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self,root):
        if not root:
            return -1
        return 1+max(self.height(root.left),self.height(root.right))

    #自底向上，遍历
    def isBalanceHelper(self,root):
        if not root:
            return True,-1
        leftIsBalance,leftHeight=self.isBalanceHelper(root.left)
        if not leftIsBalance:
            return False,0
        rightIsBalance,rightHeight=self.isBalanceHelper(root.right)
        if not rightIsBalance:
            return False,0

        return (abs(leftHeight-rightHeight)<2),1+max(leftHeight,rightHeight)

    def isBalance(self,root):
        return self.isBalanceHelper(root)[0]

if __name__ == '__main__':
    t1=TreeNode(3)
    t2 = TreeNode(20)
    t3 = TreeNode(9)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    s=Solution()
    s.isBalanced(t1)


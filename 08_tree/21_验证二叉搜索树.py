"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.mask=0
    #递归
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left:
            left_node = root.left
            while left_node.right:
                left_node = left_node.right
            if root.val < left_node.val:
                self.mask += 1
        if root.right:
            right_node = root.right
            while right_node.left:
                right_node = right_node.left
            if  right_node.val<root.val:
                self.mask+=1
        if self.mask!=0:
            return False
        else:
            return self.judge(root)

#递归同一层左子树小于根节点，右子树大于根节点，但是不够还需保证
#还需保证根节点大于左子树的最右节点，小于右节点的最左节点
    def judge(self,root):
        if not root:
            return self.mask
        if root.left:
            if root.val<=root.left.val:
                self.mask+=1
        if root.right:
            if root.right.val<=root.val:
                self.mask+=1
        self.isValidBST(root.left)
        self.isValidBST(root.right)
        if self.mask!=0:
            return False
        else:
            return True

    #官方答案1,递归
    def isValidBST1(self,root):
        def helper(node,lower=float('-inf'),upper=float('inf')):
            if not node:
                return True
            val=node.val
            if val<=lower or upper<=val:
                return False

            if not helper(node.right,val,upper):
                return False
            if not helper(node.left,lower,val):
                return False

            return True
        return helper(root)

    #官方答案2，迭代
    def isValidBS2(self,root):
        if not root:
            return True
        stack=[(root,float('-inf'),float('inf'))]
        while stack:
            root,lower,upper=stack.pop()
            if not root:
                continue
            val=root.val
            if val<=lower or val>=upper:
                return False
            stack.append((root.right,val,upper))
            stack.append((root.left,lower,val))
        return True

    # 官方答案3，中序遍历 ,中序遍历的排列恰好为二叉搜索树
    def isValidBS2(self, root):
        if not root:
            return True
        stack=[]
        inorder=float('-inf')
        tmp=root
        while tmp or stack:
            while tmp:
                stack.append(tmp)
                tmp=tmp.left
            node=stack.pop()
            if node.val<=inorder:
                return False
            inorder=node.val
            tmp=node.right


if __name__ == '__main__':
    t1=TreeNode(5)
    t2 = TreeNode(3)
    t3 = TreeNode(9)
    t4 = TreeNode(2)
    t5 = TreeNode(4)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    s=Solution()
    print(s.isValidBST1(t1))
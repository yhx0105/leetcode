"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    "访问每个字节点的时间复杂度O(n),空见复杂度O(logn)~O(n)"

    def hasPathSum(self,root,sum):
        if not root:
            return False
        sum-=root.val
        if not root.left and not root.right:
            return sum==0
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)

    "迭代"
    def hasPathSum2(self,root,sum):
        if not root:
            return False
        de=[(root,sum-root.val)]
        while de:
            node,curr_sum=de.pop()
            if not node.left and not node.right and curr_sum==0:
                return True
            if node.right:
                de.append((node.right,curr_sum-node.right.val))
            if node.left:
                de.append((node.left,curr_sum-node.left.val))
        return False

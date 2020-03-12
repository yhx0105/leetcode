"""
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #DFS，对所有节点递归 时间 O(n2)  空间 O(1)
    def pathSum(self, root: TreeNode, sum_: int) -> int:
        if not root:
            return 0
        return self.paths(root,sum_)+self.pathSum(root.left,sum_)+self.pathSum(root.right,sum_)

    def paths(self,root,sum_):
        if not root:
            return 0
        res=0
        if root.val==sum_:
            res+=1
        res+=self.paths(root.left,sum_-root.val)
        res+=self.paths(root.right,sum_-root.val)
        return res




if __name__ == '__main__':
    t1=TreeNode(3)
    t2 = TreeNode(2)
    t3 = TreeNode(9)
    t4 = TreeNode(1)
    t5 = TreeNode(7)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    s=Solution()
    print(s.pathSum(t1,5))
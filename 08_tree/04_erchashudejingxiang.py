"""
操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：源二叉树
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    	镜像二叉树
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        self.swap(root)
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root

    def swap(self,root):
        node=root.left
        root.left=root.right
        root.right=node

if __name__ == '__main__':
    t1=TreeNode(8)
    t2 = TreeNode(6)
    t3 = TreeNode(10)
    t4 = TreeNode(5)
    t5 = TreeNode(7)
    t6 = TreeNode(9)
    t7 = TreeNode(11)

    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    t3.left=t6
    t3.right=t7
    s=Solution()
    print(s.Mirror(t1))


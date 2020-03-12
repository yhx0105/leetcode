"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans=None
    #从下向上遍历,回溯  t:O(n)  p:O(n)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.helper(root,p,q)
        return self.ans


    def helper(self,root,p,q):
        if not root:
            return False
        right=self.helper(root.left,p,q)
        left=self.helper(root.right,p,q)

        if root==p or root==q:
            mid=True
        else:
            mid=False

        if mid+left+right>=2:
            self.ans=root

        return mid or left or right

    #使用父指针
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack=[root]
        parent={root:None}
        while p not in parent or q not in parent:
            node=stack.pop()
            if node.left:
                parent[node.left]=node
                stack.append(node.left)
            if node.right:
                parent[node.right]=node
                stack.append(node.right)

        ancestors=set()
        while p:
            ancestors.add(p)
            p=parent[p]
        while q not in ancestors:
            q=parent[q]
        return q


if __name__ == '__main__':
    t1=TreeNode(5)
    t2 = TreeNode(3)
    t3 = TreeNode(9)
    t4 = TreeNode(2)
    t5 = TreeNode(4)
    t6=TreeNode(6)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    t4.left=t6
    s=Solution()
    res=s.lowestCommonAncestor2(t1,t2,t6)
    print(res.val)
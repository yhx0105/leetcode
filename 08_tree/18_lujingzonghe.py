"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

"""
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.res=[]
    # 遍历思想
    def pathSum(self, root: TreeNode, sum_: int):
        if not root:
            return []
        stack=[([root.val],root)]
        res=[]
        while stack:
            tmp,node=stack.pop()
            if not node.left  and not node.right and sum(tmp)==sum_:
                res.append(tmp)
            if node.right:
                stack.append((tmp+[node.right.val],node.right))
            if node.left:
                stack.append((tmp+[node.left.val],node.left))
        return res

    # 递归
    def pathSum2(self,root,sum_):
        self.helper(root,[],sum_)
        return self.res

    def helper(self,root,tmp,sum_):
        if not root :
            return
        if not root.left and not root.right and sum_-root.val==0:
            tmp+=[root.val]
            self.res.append(tmp)
        self.helper(root.left,tmp+[root.val],sum_-root.val)
        self.helper(root.right,tmp+[root.val],sum_-root.val)


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
    res=s.pathSum2(t1,30)
    print(res)

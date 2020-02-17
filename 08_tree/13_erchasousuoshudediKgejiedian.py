"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，
按结点数值大小顺序第三小结点的值为4。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res=self.midOrder(pRoot)
        if k>len(res) or k<0:
            return None
        else:
            return res[k-1]

    def midOrder(self,pRoot):
        if not pRoot:
            return []
        stack=[]
        tmp=pRoot
        res=[]
        while stack or tmp:
            while tmp:
                stack.append(tmp)
                tmp=tmp.left
            node=stack.pop()
            res.append(node)
            tmp=node.right
        return res


if __name__ == '__main__':
    t1=TreeNode(8)
    t2=TreeNode(6)
    t3=TreeNode(10)
    t4=TreeNode(5)
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
    print(s.midOrder(t1))
    res=s.KthNode(t1,1)
    print(res)
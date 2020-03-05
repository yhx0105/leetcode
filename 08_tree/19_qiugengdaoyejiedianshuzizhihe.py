"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。
"""
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res=[]
    # 递归
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return
        self.get_num(root,[])
        sum=0
        for elem in self.res:
            tmp=0
            for i,x in enumerate(elem):
                tmp=10**(len(elem)-i-1)*x+tmp
            sum=tmp+sum
        return sum
#对于递归的理解，
    def get_num(self,root,tmp):
        if not root:
            return
        if not root.left and not root.right:
            tmp+=[root.val]
            #浅层copy，不然pop()会出来
            self.res.append(copy.copy(tmp))
            tmp.pop()
        self.get_num(root.left,tmp+[root.val])
        self.get_num(root.right,tmp+[root.val])

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
    print(s.sumNumbers(t1))
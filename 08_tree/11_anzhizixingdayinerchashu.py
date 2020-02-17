"""
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
"""
import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    #pycharm可运行，牛客报错
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack1=[pRoot]
        stack2=[]
        res=[pRoot]
        while stack1 or stack2:
            while stack1:
                tmpNode=stack1.pop()
                if tmpNode.right:
                    stack2.append(tmpNode.right)
                if tmpNode.left:
                    stack2.append(tmpNode.left)
            if len(stack2)>0:
                res.append(copy.copy(stack2))
            while stack2:
                tmpNode=stack2.pop()
                if tmpNode.left:
                    stack1.append(tmpNode.left)
                if tmpNode.right:
                    stack1.append(tmpNode.right)
            if len(stack1):
                res.append(copy.copy(stack1))
        return res

    def Print1(self, pRoot):
        # write code here
        if not pRoot:
            return []
        stack1=[pRoot]
        stack2=[]
        res=[]
        while stack1 or stack2:
            tmpList=[]
            while stack1:
                tmpNode=stack1.pop()
                tmpList.append(tmpNode.val)
                if tmpNode.left:
                    stack2.append(tmpNode.left)
                if tmpNode.right:
                    stack2.append(tmpNode.right)
            if tmpList:
                res.append(tmpList)
            tmpList=[]
            while stack2:
                tmpNode=stack2.pop()
                tmpList.append(tmpNode.val)
                if tmpNode.right:
                    stack1.append(tmpNode.right)
                if tmpNode.left:
                    stack1.append(tmpNode.left)
            if tmpList:
                res.append(tmpList)
        return res




    def dps(self,pRoot):
        if not pRoot:
            return []
        res=[]
        support=[pRoot]
        while len(support):
            node=support.pop(0)
            res.append(node.val)
            if node.left:
                support.append(node.left)
            if node.right:
                support.append(node.right)
        return res

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
    print(s.Print1(t1))
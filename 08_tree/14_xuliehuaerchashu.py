"""
请实现两个函数，分别用来序列化和反序列化二叉树


二叉树的序列化是指：
把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），
以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：
根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.pre_str=""

    def Serialize(self, root):
        # write code here

        res=self.preOrder(root)
        return res


    def preOrder(self,root):
        if not root:
            self.pre_str=self.pre_str+' '+'#'
            return self.pre_str
        self.pre_str=self.pre_str+' '+str(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
        return self.pre_str



    def Deserialize(self, s):
        # write code here
        retList=s.split()
        print(retList)
        pRoot=self.dePreOrder(retList)
        return pRoot

    def dePreOrder(self,retList):
        if not retList:
            return None
        rootVal=retList[0]
        del retList[0]
        if rootVal== "#":
            return None

        node=TreeNode(int(rootVal))
        leftNode=self.dePreOrder(retList)
        rightNode=self.dePreOrder(retList)

        node.left=leftNode
        node.right=rightNode

        return node

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
    res=s.Serialize(t1)
    print(s.Deserialize(res))
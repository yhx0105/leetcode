"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    #存储一下中序遍历，然后找出pNode的下一个值
    def GetNext1(self, pNode):
        # write code here
        if not pNode:
            return None
        dummy=pNode
        while dummy.next:
            dummy=dummy.next
        res=self.midTraversal(dummy)
        l=len(res)
        if res.index(pNode)<l-1:
            return res[res.index(pNode)+1]
        else:
            return None


    def midTraversal(self,root):
        tmplist=[]
        tmpNode=root
        res=[]
        while tmpNode or tmplist:
            while tmpNode:
                tmplist.append(tmpNode)
                tmpNode=tmpNode.left
            node=tmplist.pop()
            res.append(node)
            tmpNode=node.right
        return res

    #后序遍历
    def lastOrder(self,pNode):
        tmplist=[]
        tmpNode=pNode
        res=[]
        while tmplist or tmpNode:
            while tmpNode:
                tmplist.append(tmpNode)
                tmpNode=tmpNode.left
            node=tmplist[-1]
            tmpNode=node.right
            if not tmpNode:
                res.append(node)
                node=tmplist.pop()
                while tmplist and tmplist[-1].right==node:
                    node=tmplist.pop()
                    res.append(node)

#（1） 若该节点存在右子树：则下一个节点为右子树最左子节点
# （2） 若该节点不存在右子树：这时分两种情况：
# 2.1该节点为父节点的左子节点，则下一个节点为其父节点
# 2.2该节点为父节点的右子节点，则沿着父节点向上遍历，知道找到一个节点的父节点的左子节点为该节点，则该节点的父节点下一个节点
    def GetNext2(self, pNode):
        if pNode.right:
            tmpNode=pNode.right
            while tmpNode.left:
                tmpNode=tmpNode.left
            return tmpNode
        else:
            tmpNode=pNode
            while tmpNode.next:
                if tmpNode.next.left==tmpNode:
                    return tmpNode.next
                tmpNode=tmpNode.next
            return None


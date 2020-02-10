"""
实现树的先序，中序，后续遍历，根据根节点而言
根左右，左根右，左右根
"""
class TreeNode(object):
    def __init__(self,x):
        self.value=x
        self.left=None
        self.right=None

class Solution():
    #先序遍历
    def Traversal1(self,head):
        if head==None:
            return None
        print(head.value)
        self.Traversal1(head.left)
        self.Traversal1(head.right)

    #中序遍历
    def Traversal2(self,head):
        if head==None:
            return None
        self.Traversal2(head.left)
        print(head.value)
        self.Traversal2(head.right)

    #后续遍历
    def Traversal3(self,head):
        if head==None:
            return None
        self.Traversal3(head.left)
        self.Traversal3(head.right)
        print(head.value)

    #循环代替递归,前序遍历
    def preOrder(self,head):
        if head==None:
            return None
        stack=[]
        tmpNode=head
        while tmpNode or stack:
            while tmpNode:
                print(tmpNode.value)
                stack.append(tmpNode)
                tmpNode=tmpNode.left
            node=stack.pop()
            tmpNode=node.right

#循环代替递归,中序遍历
    def midOrder(self,head):
        if head==None:
            return None
        stack=[]
        tmp=head
        while tmp or stack:
            while tmp:
                stack.append(tmp)
                tmp=tmp.left
            node=stack.pop()
            print(node.value)
            tmp=node.right

#循环代替递归,后序遍历
    def lastOrder(self,head):
        if head==None:
            return None
        stack=[]
        tmp=head
        while tmp or stack:
            while tmp:
                stack.append(tmp)
                tmp=tmp.left
            node=stack[-1]
            tmp=node.right
            if not tmp:
                print(node.value)
                node=stack.pop()
                while stack and node ==stack[-1].right:
                    node=stack.pop()
                    print(node.value)




if __name__ == '__main__':
    t1=TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)

    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    t3.left=t6
    t3.right=t7
    t6.right=t8

    s=Solution()
    print(s.lastOrder(t1))
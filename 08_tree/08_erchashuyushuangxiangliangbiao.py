"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree==None:
            return []
        stack=[]
        res=[]
        tmp=pRootOfTree
        while tmp or stack:
            while tmp:
                stack.append(tmp)
                tmp=tmp.left
            node=stack.pop()
            res.append(node)
            tmp=node.right
        resP=res[0]
        while res:
            top=res.pop()
            if res:
                top.right=res[0]
                res[0].left=top
        return resP

    #递归
    def Convert1(self, pRootOfTree):
        if pRootOfTree==None:
            return None

        # 将左子树构建成双链表，返回链表头
        left=self.Convert1(pRootOfTree.left)
        p=left

        #定位到左子树最左边节点
        while left and p.right:
            p=p.right

        #如果左子树不为空，当前root加到左子树列表
        if left:
            p.right=pRootOfTree
            pRootOfTree.left=p

        #将左子树构成双向链表
        right=self.Convert1(pRootOfTree.right)
        #如果左子树不为空，该链表加到根节点之后
        if right:
            right.left=pRootOfTree
            pRootOfTree.right=right

        if left:
            return left
        else:
            return pRootOfTree


if __name__ == '__main__':
    t1=TreeNode(5)
    t2=TreeNode(2)
    t3=TreeNode(1)
    t4=TreeNode(16)
    t5 = TreeNode(3)
    t6 = TreeNode(0)
    t7 = TreeNode(15)
    t1.left=t2
    t2.left=t3
    t2.right=t4
    t1.right=t5
    t5.left=t6
    t6.right=t7
    s=Solution()
    res=s.Convert(t1)
    print(res)
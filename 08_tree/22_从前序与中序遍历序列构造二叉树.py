"""
根据一棵树的前序遍历与中序遍历构造二叉树。
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #前序遍历的第一个节点为根节点，中序遍历找到根节点可以分左右子树，递归
    #时间复杂度O(n)   空间复杂度O(n)
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder or not inorder:
            return None
        if len(preorder)!=len(inorder):
            return None

        root=preorder[0]
        rootNode=TreeNode(root)
        pos=inorder.index(root)

        pre_left=preorder[1:pos+1]
        pre_right=preorder[pos+1:]

        in_left=inorder[:pos]
        in_right=inorder[pos+1:]

        leftNode=self.buildTree(pre_left,in_left)
        rightNode=self.buildTree(pre_right,in_right)

        if leftNode:
            rootNode.left=leftNode
        if rightNode:
            rootNode.right=rightNode
        return rootNode


if __name__ == '__main__':
    a=['a','b','c','d']
    print(a.index('a'))



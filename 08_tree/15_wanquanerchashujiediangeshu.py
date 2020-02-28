"""完全二叉树的定义如下：
在完全二叉树中，除了最底层节点可能没填满外，
其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层，则该层包含 1~ 2h 个节点。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    #广度优先
    def countNodes1(self, root):
        if not root:
            return 0
        tmplist=[]
        tmplist.append(root)
        res=[]
        while len(tmplist):
            node=tmplist.pop(0)
            res.append(node.val)
            if node.left:
                tmplist.append(node.left)
            if node.right:
                tmplist.append(node.right)
        return len(res)

    """
     完全二叉树的高度可以直接通过不断地访问左子树就可以获取
        判断左右子树的高度: 
        如果相等说明左子树是满二叉树, 然后进一步判断右子树的节点数(最后一层最后出现的节点必然在右子树中)
        如果不等说明右子树是深度小于左子树的满二叉树, 然后进一步判断左子树的节点数(最后一层最后出现的节点必然在左子树中)
    """
    def countNodes2(self, root):
        if not root:
            return 0
        lh,lr=self.getheight(root.left),self.getheight(root.right)
        if lh==lr:
            return pow(2,lh)-1+1+self.countNodes2(root.right)
        else:
            return pow(2,lh)-1+1+self.countNodes2(root.left)

    def getheight(self,root):
        ret=0
        while root:
            ret +=1
            root=root.left
        return ret

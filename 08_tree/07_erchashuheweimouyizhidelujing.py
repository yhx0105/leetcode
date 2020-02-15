"""
输入一颗二叉树的根节点和一个整数，
打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    #DPS
    def FindPath(self, root, expectNumber):
        # write code here
        if root==None:
            return []
        res=[]

        def FindPathMain(root,path,currentSum):
            currentSum+=root.val
            path.append(root)
            if root.left==None and root.right==None:
                isLeaf=True
            else:
                isLeaf=False

            if currentSum==expectNumber and isLeaf:
                onePath=[]
                for node in path:
                    onePath.append(node.val)
                res.append(onePath)

            if currentSum<expectNumber:
                if root.left:
                    FindPathMain(root.left,path,currentSum)
                if root.right:
                    FindPathMain(root.right,path,currentSum)
            path.pop()
        FindPathMain(root,[],0)
        return res

    #DFS
    def FindPath1(self, root, expectNumber):
        if root==None:
            return []
        res=[]
        support=[root]
        supportArrayList=[[root.val]]
        while len(support):
            node=support.pop(0)
            res.append(node)
            tmpArrayList=supportArrayList[0]
            if node.left==None and node.right==None:
                if sum(tmpArrayList)==expectNumber:
                    res.insert(0,tmpArrayList)
            if node.left:
                support.append(node.left)
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(node.left.val)
                supportArrayList.append(newTmpArrayList)
            if node.right:
                support.append(node.right)
                newTmpArrayList = copy.copy(tmpArrayList)
                newTmpArrayList.append(node.right.val)
                supportArrayList.append(newTmpArrayList)
            del supportArrayList[0]
        return res




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
    res=s.FindPath1(t1,23)
    for i in res:
        print(i)
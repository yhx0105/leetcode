"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
二叉搜索树
如果节点的左子树不空，则左子树上所有结点的值均小于等于它的根结点的值；
如果节点的右子树不空，则右子树上所有结点的值均大于等于它的根结点的值；
任意节点的左、右子树也分别为二叉查找树
"""
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence==None or len(sequence)==0:
            return False
        length=len(sequence)
        root=sequence[-1]
        for i in range(length):
            if sequence[i]>root:
                break


        for j in range(i,length):
            if sequence[j]<root:
                return False

        left=True
        if i>0:
            left=self.VerifySquenceOfBST(sequence[:i])
        right=True
        if i <length-1:
            right=self.VerifySquenceOfBST(sequence[i:-1])
        return left and right

if __name__ == '__main__':
    sequence=[4,8,6,12,16,14,10]
    s=Solution()
    a=sequence[2:-1]
    b=sequence[2:]
    print(a,b)
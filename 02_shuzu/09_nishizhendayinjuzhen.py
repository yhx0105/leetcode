"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
# -*- coding:utf-8 -*-
class Solution:
    # matrix为矩阵，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res=[]
        while matrix:
            res+=matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res+=matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res
    """
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作 
  例如  
  1 2 3 
  4 5 6 
  7 8 9 
  输出并删除第一行后，再进行一次逆时针旋转，就变成： 
  6 9 
  5 8 
  4 7 
  继续重复上述操作即可。 """
    def printMatrix1(self,matrix):
        res=[]
        while  matrix:
            res+=matrix.pop(0)
            matrix=list(map(list,zip(*matrix)))[::-1]
        return res




if __name__ == '__main__':
    nums=[[1,2,3],[4,5,6],[7,8,9]]
    # z=zip(*nums)
    # print(list(z)[::-1])
    # res=map(list,zip(nums))
    s=Solution()
    res=s.printMatrix1(nums)
    print(res)
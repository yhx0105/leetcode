"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，
并且使皇后彼此之间不能相互攻击。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
class Solution:
    #dfs  t:O(n!)  s:O(n)
    def __init__(self):
        self.res=0

    def totalNQueens(self, n: int):
        cols=[0]*n
        hill_diagonals=[0]*(2*n-1)
        dale_diagonals=[0]*(2*n-1)
        queens=set()
        output=[]
        def dfs(row=0):
            for col in range(n):
                if could_place(row,col):
                    place_queen(row,col)
                    if row+1==n:
                        self.res+=1
                    else:
                        dfs(row+1)
                    remove_queen(row,col)

        def could_place(row,col):
            return not (cols[col]+hill_diagonals[row-col]+dale_diagonals[row+col])

        def place_queen(row,col):
            queens.add((row,col))
            cols[col]=1
            hill_diagonals[row-col]=1
            dale_diagonals[row+col]=1

        def remove_queen(row,col):
            queens.remove((row,col))
            cols[col]=0
            hill_diagonals[row-col]=0
            dale_diagonals[row+col]=0

        dfs()
        return self.res
if __name__ == '__main__':
    num=4
    s=Solution()
    res=s.totalNQueens(num)
    print(res)

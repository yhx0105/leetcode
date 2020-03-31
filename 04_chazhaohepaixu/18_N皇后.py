"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，
并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，
该方案中 'Q' 和 '.' 分别代表了皇后和空位。
示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
"""
class Solution:
    #dfs  t:O(n!)  s:O(n)
    def __init__(self):
        self.res=0

    def solveNQueens(self, n: int):

        def backtrack(row=0):
            for col in range(n):
                if could_place(row,col):
                    place_queen(row,col)
                    if row+1==n:
                        self.res+=1
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row,col)

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

        def could_place(row,col):
            return not (cols[col]+hill_diagonals[row-col]+dale_diagonals[row+col])

        def add_solution():
            solution=[]
            for _,col in sorted(queens):
                solution.append('.'*col+'Q'+'.'*(n-col-1))
            output.append(solution)

        cols=[0]*n
        hill_diagonals=[0]*(2*n-1)
        dale_diagonals=[0]*(2*n-1)
        queens=set()
        output=[]
        backtrack()
        res=0
        return self.res
if __name__ == '__main__':
    n=4
    s=Solution()
    print(s.solveNQueens(n))
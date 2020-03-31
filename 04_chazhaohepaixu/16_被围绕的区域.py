"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，
并将这些区域里所有的 'O' 用 'X' 填充。
示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
"""
class Solution:
    #dfs 从边界往里面找
    def solve(self, board) :
        """
        Do not return anything, modify board in-place instead.
        """
        if board==[]:
            return board
        w=len(board)
        l=len(board[0])
        for r in range(w):
            for c in range(l):
                if r==0 or r==w-1 or c==0 or c==l-1:
                    if board[r][c]=='O':
                        self.__iterate(r,c,w,l,board)

        for r in range(w):
            for c in range(l):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='#':
                    board[r][c]='O'


    def __iterate(self,r,c,w,l,board):
        if r<0 or c<0 or r>=w or c>=l or board[r][c]=='#' or board[r][c]=='X':
            return
        board[r][c]='#'
        self.__iterate(r-1,c,w,l,board)
        self.__iterate(r+1,c,w,l,board)
        self.__iterate(r,c-1,w,l,board)
        self.__iterate(r,c+1,w,l,board)

if __name__ == '__main__':
    board=[["O","O"],["O","O"]]
    s=Solution()
    print(s.solve(board))
"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
"""


class Solution:
    #二维搜索
    def __init__(self):
        self.direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board, word):
        w = len(board)
        l = len(board[0])
        used = [[False for _ in range(l)] for _ in range(w)]

        def dfs(board, start_x, start_y, used, depth, m, n):
            if depth == len(word) - 1:
                return board[start_x][start_y] == word[depth]

            if board[start_x][start_y] == word[depth]:
                used[start_x][start_y] = True
                for direction in self.direction:
                    new_x = start_x + direction[0]
                    new_y = start_y + direction[1]
                    if 0 <= new_x < m and 0 <= new_y < n and not used[new_x][new_y] and dfs(board,  new_x, new_y,
                                                                                            used, depth + 1, m, n):
                        return True
                used[start_x][start_y]=False
            return False
        for i in range(w):
            for j in range(l):
                if dfs(board,i,j,used,0,w,l):
                    return True
        return False



if __name__ == '__main__':
    board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word="ABCCED"
    s=Solution()
    print(s.exist(board,word))
    a=[[False]*7]*7
    print(a)

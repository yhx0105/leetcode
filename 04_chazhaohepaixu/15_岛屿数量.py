"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，
计算岛屿的数量。一个岛被水包围，
并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。
输入:
11110
11010
11000
00000

输出: 1

输入:
11000
11000
00100
00011

输出: 3
"""
class Solution:
    def numIslands(self, grid):
        w=len(grid)
        l=len(grid[0])
        res=0
        for r in range(w):
            for c in range(l):
                if grid[r][c]=='1':
                    res+=1
                    self.__iterater(r,c,grid,w,l)
        return res

    def __iterater(self,r,c,grid,w,l):
        if r<0 or c<0 or r>=w or c>=l:
            return
        if grid[r][c]=='0':
            return
        grid[r][c]='0'
        self.__iterater(r-1,c,grid,w,l)
        self.__iterater(r+1,c,grid,w,l)
        self.__iterater(r,c-1,grid,w,l)
        self.__iterater(r,c+1,grid,w,l)

if __name__ == '__main__':
    grid=[["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    s=Solution()
    print(s.numIslands(grid))
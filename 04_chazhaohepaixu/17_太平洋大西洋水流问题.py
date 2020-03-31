"""
难度中等85给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。
“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

提示：
输出坐标的顺序不重要
m 和 n 都小于150

给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

"""


class Solution:
    def __init__(self):
        self.res_all=None
        self.direct=[(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.m=0
        self.n=0
        #流入太平洋
        self.po=None
        #流入大西洋
        self.ao=None
        self.visited=None

    def pacificAtlantic(self, matrix):
        self.res_all=[]
        self.m=len(matrix)
        if self.m==0:
            return self.res_all
        self.n=len(matrix[0])
        self.ao=[[0]*self.n for _ in range(self.m)]
        self.po=[[0]*self.n for _ in range(self.m)]

        #从上方进入太平洋
        self.visited = [[0] * self.n for _ in range(self.m)]
        for i in range(0,1):
            for j in range(self.n):
                self.dfs(matrix,i,j,True)
        #从左边流入太平洋
        self.visited=[[0]*self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(0,1):
                self.dfs(matrix,i,j,True)
        #从下面溜入大西洋
        self.visited=[[0]*self.n for _ in range(self.m)]
        for i in range(self.m-1,self.m):
            for j in range(self.n):
                self.dfs(matrix,i,j,False)
        #从右边流入大西洋
        self.visited=[[0]*self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n-1,self.n):
                self.dfs(matrix,i,j,False)

        for i in range(self.m):
            for j in range(self.n):
                if self.po[i][j]==1 and self.ao[i][j]==1:
                    self.res_all.append((i,j))

        return self.res_all

    def dfs(self, matrix,x,y,flag):
        if self.visited[x][y]==1:
            return
        self.visited[x][y]=1
        if flag:
            self.po[x][y]=1
        else:
            self.ao[x][y]=1
        for i in range(4):
            newx = x + self.direct[i][0]
            newy = y + self.direct[i][1]
            if not self.in_area(newx,newy):
                continue
            #如果旁边的数小于当前数字，不能流入
            if matrix[x][y]>matrix[newx][newy]:
                continue
            self.dfs(matrix,newx,newy,flag)
        return

    def in_area(self,x,y):
        return 0 <= x < self.m and 0 <= y < self.n

if __name__ == '__main__':
    a = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    s=Solution()
    print(s.pacificAtlantic(a))

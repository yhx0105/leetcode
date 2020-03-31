"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""
class Solution:
    #递归 时间Olog(n)
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

    #递归改循环
    def climbStairs2(self,n):
        if n<=2:
            return n
        a=1
        b=2
        for i in range(3,n+1):
            ret=a+b
            a=b
            b=ret
        return ret

    #动态规划法
    def climbStairs3(self,n):
        if n==1:
            return 1
        tmp=[1,2]
        for i in range(2,n):
            tmp.append(tmp[i-1]+tmp[i-2])
        return tmp[-1]

if __name__ == '__main__':
    s=Solution()
    print(s.climbStairs3(4))
"""
首先,让小朋友们围成一个大圈。
然后,他随机指定一个数m,让编号为0的小朋友开始报数。
每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,
并且不再回到圈中,从他的下一个小朋友开始,
继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,
并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)
"""
class Solution:
    #列表的思想，列表构建循环，复杂度O(mn)
    def LastRemaining_Solution1(self, n, m):
        # write code here
        if n==0:
            return -1
        if n==1:
            return 0
        cur=0
        childlist=list(range(n))
        while len(childlist)>1:
            for i in range(1,m):
                cur=cur+1
                if cur==len(childlist):
                    cur=0
            childlist.remove(childlist[cur])
            if cur==len(childlist):
                cur=0
        return childlist[0]

    #递归f(n)=(f(n-1)+m)%n
    def LastRemaining_Solution2(self, n, m):
        if n==1:
            return 0
        elif n==0:
            return -1
        else:
            return (self.LastRemaining_Solution2(n-1,m)+m)%n

    #递归改循环
    def LastRemaining_Solution3(self, n, m):
        if n==1:
            return 0
        elif n==0:
            return -1
        else:
            value=0
            for i in range(2,n+1):
                value=(value+m)%i
            return value



if __name__ == '__main__':
    s=Solution()
    print(s.LastRemaining_Solution1(5,3))
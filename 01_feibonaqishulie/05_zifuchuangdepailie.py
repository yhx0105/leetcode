"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串
abc,acb,bac,bca,cab和cba。
"""
import copy
class Solution:
    def __init__(self):
        """
        [n,size]位置的数字全排
        [n]要交换的位置
        result:保留结果
        """
        self.start=0
        self.n=0
        self.result=[]

    #全排列
    def Permutation1(self, ss):
        if self.n==len(ss):
            self.result.append(copy.deepcopy(ss))
        for i in range(len(ss)):
            if self.isduplicate(ss,self.n,i):
                continue
            self.swap(ss,i,self.n)
            self.n=self.n+1
            self.Permutation1(ss)
            self.swap(ss,i,self.n)

    #判断第n个字符与第一个是否相同
    def isduplicate(self,ss,n,i):
        """
        :param ss:
        :param n: n为开始的点
        :param i: 第i个需要交换的点
        :return:
        """
        while n<i:
            if ss[n]==ss[i]:
                return True
            n+=1
        return False

    def swap(self,ss,start,i):
        if start==i:
            return
        ss[i],ss[start]=ss[start],ss[i]

    def Permutation(self, ss):
        # write code here
        if len(ss)<=1:
            return ss
        res=set()
        for i in range(len(ss)):
            tmp=self.Permutation(ss[:i]+ss[i+1:])
            for j in tmp:
                res.add(ss[i]+j)
        return sorted(res)


if __name__ == '__main__':
    ss="abc"
    s=Solution()
    print(s.Permutation(ss))


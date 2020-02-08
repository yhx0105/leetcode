"""
求出1~13的整数中1出现的次数,
并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有
1、10、11、12、13因此共出现6次,
但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数
（从1 到 n 中1出现的次数）。
"""
class Solution:
    #统计含有1的次数,暴力破解
    def NumberOf1Between1AndN_Solution1(self, n):
        # write code here
        res=[]
        for i in range(1,n+1):
            res.append(str(i))
        count=0
        for elem in res:
            for tar in elem:
                if tar=='1':
                    count+=1
        return count

    #递归,f(n)=f(n-1)+count(n)
    def NumberOf1Between1AndN_Solution2(self, n):
        count = 0
        while n>1:
            for i in str(n):
                if i=='1':
                    count+=1
            return count+self.NumberOf1Between1AndN_Solution2(n-1)
        return 1


    #递归改循环
    def NumberOf1Between1AndN_Solution3(self, n):
        count=0
        res=0
        for i in range(1,n+1):
            for e in str(i):
                if e=='1':
                    count+=1
            res=count+res
            count=0
        return res

    #位数,效果最好
    """
    设定整数点（如1、10、100等等）
    作为位置点i（对应n的各位、十位、百位等等），
    分别对每个数位上有多少包含1的点进行分析 .
    """
    def NumberOf1Between1AndN_Solution4(self, n):
        highValue=1
        midValue=1
        lowValue=1
        precise=1
        count=0
        sumnum=0
        while highValue!=0:
            highValue=n//(precise*10)
            midValue=(n//precise)%10
            lowValue=n%precise
            precise=precise*10

            if midValue==0:
                num=highValue*pow(10,count)
            elif midValue>1:
                num=(highValue+1)*pow(10,count)
            else:
                num=highValue*pow(10,count)+lowValue+1
            sumnum=num+sumnum
            count+=1
        return sumnum

if __name__ == '__main__':
    s=Solution()
    print(s.NumberOf1Between1AndN_Solution4(5))

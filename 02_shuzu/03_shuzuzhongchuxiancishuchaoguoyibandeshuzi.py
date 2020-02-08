"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
如果不存在则输出0。
"""
class Solution:
    #把两个不同的数去掉，剩下那个可能是目标数，再进行判断
    def MoreThanHalfNum_Solution1(self, numbers):
        # write code here
        last=0
        lastCount=0
        for num in numbers:
            if lastCount==0:
                last=num
                lastCount=1
            else:
                if num==last:
                    lastCount+=1
                else:
                    lastCount-=1
        if lastCount==0:
            return 0
        else:
            #可能是大于一半数字
            lastCount=0
            for num in numbers:
                if num==last:
                    lastCount+=1
            if lastCount>len(numbers)//2:
                return last
            else:
                return 0

    #字典
    def MoreThanHalfNum_Solution12(self, numbers):
        dic={}
        for num in numbers:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
            if dic[num]>len(numbers)//2:
                return num
        return 0



if __name__ == '__main__':
    numbers=[1,2,3,2,2,2,5,4,2]
    s=Solution()
    print(s.MoreThanHalfNum_Solution(numbers))

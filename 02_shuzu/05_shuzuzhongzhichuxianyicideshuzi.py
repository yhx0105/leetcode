"""
一个整型数组里除了两个数字之外，
其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    #字典
    def FindNumsAppearOnce1(self, array):
        # write code here
        double={}
        res=[]
        for elem in array:
            if elem in double:
                double[elem]+=1
            else:
                double[elem]=1
        for elem in double:
            if double[elem]==1:
                res.append(elem)
        return res

    #异或,1.a^b^c=c^b^a  满足交换律  2.两个相同数异或值为0
    def FindNumsAppearOnce2(self, array):
        twoNumXor=None
        for elem in array:
            if twoNumXor==None:
                twoNumXor=elem
            else:
                twoNumXor=twoNumXor^elem
        count=0
        while twoNumXor%2==0:
            twoNumXor=twoNumXor>>1
            count+=1
        mask=1<<count
        firstNum=None
        secondNum=None
        for num in array:
            if mask&num==0:
                if firstNum==None:
                    firstNum=num
                else:
                    firstNum=firstNum^num
            else:
                if secondNum==None:
                    secondNum=num
                else:
                    secondNum=secondNum^num
        return [firstNum,secondNum]

if __name__ == '__main__':
    s=Solution()
    a=[1,2,33,33,4,4]
    print(s.FindNumsAppearOnce2(a))
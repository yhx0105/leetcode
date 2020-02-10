"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
class Solution:
    def GetUglyNumber_Solution1(self, index):
        # write code here
        if index==1 or index==0:
            return index
        pointer2=0
        pointer3=0
        pointer5=0
        l=[1]
        count=0
        while count<index-1:
            newNum=min(l[pointer2]*2,l[pointer3]*3,l[pointer5]*5)
            if newNum==l[pointer2]*2:
                pointer2+=1
            if newNum==l[pointer3]*3:
                pointer3+=1
            if newNum==l[pointer5]*5:
                pointer5+=1
            count+=1
            l.append(newNum)
        return l[-1]

    #暴力法，判断一个属能否被2，3，5整除于1
    def GetUglyNumber_Solution2(self, index):
        def isUglyNumber(index):
            while index%2==0:
                index=index//2
            while index%3==0:
                index=index//3
            while index%5==0:
                index=index//5
            if index==1:
                return True
            else:
                return False
        num=1
        count=0
        while True:
            if isUglyNumber(num):
                count+=1
            if count==index:
                return num
            num+=1



if __name__ == '__main__':
    s=Solution()
    print(s.GetUglyNumber_Solution1(9))


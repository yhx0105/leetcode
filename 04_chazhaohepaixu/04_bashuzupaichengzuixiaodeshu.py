"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
"""
import copy
class Solution:
    #归并排序
    def PrintMinNumber1(self, numbers):
        # write code here
        l1=len(numbers)
        out=self.sortMerge(numbers)
        if len(out)==l1:
            print(out)
            res=""
            for elem in out:
                res=res+str(elem)

            return int(res)


    def sortMerge(self,numbers):
        l=len(numbers)
        if l==1:
            return numbers
        if l==0:
            return []
        midIndex=l//2
        sorted_left=self.sortMerge(numbers[:midIndex])
        sorted_right=self.sortMerge(numbers[midIndex:])

        return self.gettMergeCore(sorted_left,sorted_right)


    def gettMergeCore(self,leftList,rightList):
        leftP=0
        rightP=0
        lt=len(leftList)
        lr=len(rightList)
        retList=[]
        while leftP<lt and rightP<lr:
            if leftList[leftP]<rightList[rightP]:
                retList.append(leftList[leftP])
                leftP+=1
            else:
                retList.append(rightList[rightP])
                rightP+=1
        while leftP<lt:
            retList.append(leftList[leftP])
            leftP+=1
        while rightP<lr:
            retList.append(rightList[rightP])
            rightP+=1
        return retList

if __name__ == '__main__':
    nums=[35,33,42,10,14,19,27,44]
    s=Solution()
    res=s.PrintMinNumber1(nums)
    print(res)
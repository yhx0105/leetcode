"""
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
"""
class Solution:
    def __init__(self):
        self.res=0
    #时间复杂度过大
    def InversePairs1(self, data):
        # write code here
        count=0
        l=len(data)
        for i in range(l):
            for j in range(i,l):
                if data[i]>data[j]:
                    count+=1
        return count%1000000007

    #归并排序
    def InversePairs2(self, data):
        self.mergeSort(data)
        return self.res

    def mergeSort(self,data):
        l=len(data)
        if l==1:
            return data
        if l<1:
            return []
        midIndex=l//2
        sortedLeft=self.mergeSort(data[:midIndex])
        sortedRight=self.mergeSort(data[midIndex:])
        self.mergetCore(sortedLeft,sortedRight)

    def mergetCore(self,sortedLeft,sortedRight):
        leftP=0
        rightP=0
        lf=len(sortedLeft)
        lr=len(sortedRight)
        tmplist=[]
        while leftP<lf and rightP<lr:
            if sortedRight[rightP]<sortedLeft[leftP]:
                self.res+=1
                tmplist.append(sortedLeft[leftP])
                leftP+=1
            else:
                tmplist.append(sortedRight[rightP])
                rightP+=1
        while leftP<lf:
            self.res+=lr
            tmplist.append(sortedLeft[leftP])
            leftP+=1
        while rightP<lr:
            tmplist.append(sortedRight[rightP])
            rightP+=1
        return tmplist

if __name__ == '__main__':
    data=[5,6,3]
    s=Solution()
    print(s.InversePairs2(data))
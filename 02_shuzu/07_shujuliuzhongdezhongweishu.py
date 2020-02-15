"""
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，
那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，
使用GetMedian()方法获取当前读取数据的中位数。
"""
class Solution:
    def __init__(self):
        self.arr=[]
        #堆排序
        self.minNums=[]
        self.maxNums=[]
        self.maxHeapCount=0
        self.minHeapCount=0

    def Insert1(self, num):
        # write code here
        self.arr.append(num)
        self.arr.sort()

    def GetMedian1(self):
        # write code here
        l=len(self.arr)
        index=l//2
        if l%2==0:
            return (self.arr[index]+self.arr[index-1])/2
        else:
            return self.arr[index]

    #堆排序
    #构建最大堆存储较小的数
    def maxHeapInset(self,num):
        self.maxNums.append(num)
        currentIndex=len(self.maxNums)-1
        while currentIndex!=0:
            parentIndex=(currentIndex-1)//2
            if self.maxNums[currentIndex]>self.maxNums[parentIndex]:
                self.maxNums[currentIndex],self.maxNums[parentIndex]=self.maxNums[parentIndex],self.maxNums[currentIndex]
                currentIndex=parentIndex
            else:
                break

    def maxHeapJust(self,num):
        if num<self.maxNums[0]:
            self.maxNums[0]=num
            lens=len(self.maxNums)
            index=0
            while index<lens:
                leftIndex=index*2+1
                rightIndex=index*2+2
                largerIndex=0
                if rightIndex<lens:
                    if self.maxNums[rightIndex]<self.maxNums[leftIndex]:
                        largerIndex=leftIndex
                    else:
                        largerIndex=rightIndex
                elif leftIndex<lens:
                    largerIndex=leftIndex
                else:
                    break
                if self.maxNums[index]<self.maxNums[largerIndex]:
                    self.maxNums[index],self.maxNums[largerIndex]=self.maxNums[largerIndex],self.maxNums
                    index=largerIndex
                else:
                    break

    #构建最小堆，存储较大的数
    def minHeapInset(self,num):
        self.minNums.append(num)
        currentIndex=len(self.minNums)-1
        while currentIndex!=0:
            parentIndex=(currentIndex-1)//2
            if self.minNums[currentIndex]<self.minNums[parentIndex]:
                self.minNums[currentIndex],self.minNums[parentIndex]=self.minNums[parentIndex],self.minNums[currentIndex]
                currentIndex=parentIndex
            else:
                break

    def minHeapJust(self,num):
        if self.maxNums[0]<num:
            self.maxNums[0]=num
            lens=len(self.maxNums)
            index=0
            while index<lens:
                leftIndex=index*2+1
                rightIndex=index*2+2
                smallerIndex=0
                if rightIndex<lens:
                    if self.maxNums[rightIndex]<self.maxNums[leftIndex]:
                        smallerIndex=rightIndex
                    else:
                        smallerIndex=leftIndex
                elif leftIndex<lens:
                    smallerIndex=leftIndex
                else:
                    break
                if self.maxNums[smallerIndex]<self.maxNums[index]:
                    self.maxNums[index],self.maxNums[smallerIndex]=self.maxNums[smallerIndex],self.maxNums
                    index=smallerIndex
                else:
                    break
    def Insert2(self,num):
        if self.maxHeapCount<self.minHeapCount:
            self.minHeapCount+=1
            if len(self.minNums)==0:
                self.minHeapInset(num)
            else:
                if num<self.minNums[0]:
                    tmpNum=self.minNums[0]
                    self.minHeapJust(num)
                    self.minHeapInset(tmpNum)
                else:
                    self.minHeapInset(num)
        else:
            self.maxHeapCount+=1
            if len(self.maxNums)==0:
                self.maxHeapInset(num)
            else:
                if self.maxNums[0]<num:
                    tmpNum=self.maxNums[0]
                    self.maxHeapJust(num)
                    self.maxHeapInset(tmpNum)
                else:
                    self.maxHeapInset(num)
        print(self.minNums)
        print(self.maxNums)

    def GetMedian2(self):
        if self.minHeapCount<self.maxHeapCount:
            return self.minNums[0]
        else:
            return (self.minNums[0]+self.maxNums[0])/2.0


if __name__ == '__main__':
    s=Solution()
    s.Insert2(5)
    print(s.GetMedian2())
    s.Insert2(2)
    print(s.GetMedian2())
    s.Insert2(3)
    print(s.GetMedian2())
    s.Insert2(4)
    print(s.GetMedian2())
    s.Insert2(1)
    print(s.GetMedian2())
    s.Insert2(6)
    print(s.GetMedian2())
    s.Insert2(7)
    print(s.GetMedian2())
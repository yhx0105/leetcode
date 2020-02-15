"""
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1,2,3,4,。
"""
class Solution:
    #排序，取前K个
    def GetLeastNumbers_Solution1(self, tinput, k):
        # write code here
        new_list=sorted(tinput)
        if k>len(new_list):
            return []
        else:
            return new_list[:k]

    #最大堆，创建最大堆，插入
    def GetLeastNumbers_Solution2(self, tinput, k):

        maxHeap=[]
        #创建最大堆
        def creatMaxHeap(num):
            maxHeap.append(num)
            currentIndex=len(maxHeap)-1
            while currentIndex !=0:
                parentIndex=(currentIndex-1)>>1
                if maxHeap[parentIndex]<maxHeap[currentIndex]:
                    maxHeap[parentIndex],maxHeap[currentIndex]=maxHeap[currentIndex],maxHeap[parentIndex]
                    currentIndex=parentIndex
                else:
                    break
        #调整最大堆
        def adjustMaxHeap(num,k):
            if num<maxHeap[0]:
                maxHeap[0]=num
            maxHeapLen=len(maxHeap)
            index=0
            while index<maxHeapLen:
                leftIndex=index*2+1
                rightIndex=index*2+2
                largerIndex=0
                if rightIndex<maxHeapLen:
                    if maxHeap[rightIndex]<maxHeap[leftIndex]:
                        largerIndex=leftIndex
                    else:
                        largerIndex=rightIndex
                elif leftIndex<maxHeapLen:
                    largerIndex=leftIndex
                else:
                    break
                if maxHeap[index]<maxHeap[largerIndex]:
                    maxHeap[index],maxHeap[largerIndex]=maxHeap[largerIndex],maxHeap[index]
                index=largerIndex

        l=len(tinput)

        if l<k or k<1:
            return []

        for i in range(l):
            if i <k:
                creatMaxHeap(tinput[i])
            else:
                adjustMaxHeap(tinput[i],k)
        maxHeap.sort()
        return maxHeap


if __name__ == '__main__':
    tinput=[4,5,1,6,2,7,3,8]
    k=4
    s=Solution()
    s.GetLeastNumbers_Solution2(tinput,k)
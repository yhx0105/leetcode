class Solution():
    #希尔排序
    def xier_sort(self,nums):
        l=len(nums)
        h=1
        while h<l/3:
            h=h*3+1
        while h>=1:
            for i in range(h,l):
                j=i
                while j>=h and nums[j]<nums[j-h]:
                    nums[j],nums[j-h]=nums[j-h],nums[j]
                    j-=h
            h=h//3
        return nums

    # 归并排序
    def mergeSort(self,nums):
        l=len(nums)
        if l==1:
            return nums
        if l<1:
            return []
        midIndex=l//2
        sortedLeft=self.mergeSort(nums[:midIndex])
        sortedRight=self.mergeSort(nums[midIndex:])
        return self.mergetCore(sortedLeft,sortedRight)

    def mergetCore(self,leftList,rightList):
        leftP=0
        rightP=0
        lf=len(leftList)
        lr=len(rightList)
        retList=[]
        while leftP<lf and rightP<lr:
            if leftList[leftP]<rightList[rightP]:
                retList.append(leftList[leftP])
                leftP+=1
            else:
                retList.append(rightList[rightP])
                rightP+=1
        while leftP<lf:
            retList.append(leftList[leftP])
            leftP+=1
        while rightP<lr:
            retList.append(rightList[rightP])
            rightP+=1
        return retList

    #快速排序
    def fastSort(self,nums,left,right):
        if left<right:
            pivot=self.partition(nums,left,right)
            self.fastSort(nums,left,pivot-1)
            self.fastSort(nums,pivot+1,right)

    def partition(self,nums,left,right):
        i=left
        j=right-1
        while i<j:
            while i<right and nums[i]<=nums[right]:
                i+=1
            while j>left and nums[right]<nums[j]:
                j-=1
            if i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        if nums[right]<nums[i]:
            nums[i],nums[right]=nums[right],nums[i]
        return i




if __name__ == '__main__':
    nums=[35,33,42,10,14,19,27,44]
    s=Solution()
    s.fastSort(nums,0,7)
    print(nums)

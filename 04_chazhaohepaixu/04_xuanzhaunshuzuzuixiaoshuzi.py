"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
class Solution:
    #暴力法
    def minNumberInRotateArray1(self, rotateArray):
        # write code here
        l=len(rotateArray)
        min_t=rotateArray[0]
        for i in range(l-1):
            if min_t>rotateArray[i+1]:
               min_t=rotateArray[i+1]
        return min_t

    #二分法
    def minNumberInRotateArray2(self, rotateArray):
        l=len(rotateArray)
        left=0
        right=l-1
        while right-left>1:
            mid = (left + right) // 2
            if rotateArray[left]>rotateArray[mid]:
                right=mid
            else:
                left=mid
        return rotateArray[right]

if __name__ == '__main__':
    rotateArray=[1,1, 1,0,1]
    s=Solution()
    print(s.minNumberInRotateArray2(rotateArray))
    pass
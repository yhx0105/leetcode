"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
class Solution:
    #把奇数偶数找出来，再拼在一起
    def reOrderArray1(self, array):
        # write code here
        oder=[]
        double=[]
        for i in range(len(array)):
            if array[i]%2==0:
                double.append(array[i])
            else:
                oder.append(array[i])
        oder.extend(double)
        return oder

    #冒泡排序法 偶数后移
    def reOrderArray2(self, array):
        l=len(array)-1
        for j in range(l):
            for i in range(j,l):
                if array[i]%2==0 and array[i+1]%2==1 :
                    array[i],array[i+1]=array[i+1],array[i]
        return array



if __name__ == '__main__':
    array=[2,4,6,1,3,5,7]
    s=Solution()
    print(s.reOrderArray2(array))

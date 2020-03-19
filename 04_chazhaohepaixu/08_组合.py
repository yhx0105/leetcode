"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能
的 k 个数的组合。
"""
class Solution:
    #回溯,注意 与全排列类似，但不是全排列
    #时间 O(kCnk)  空间O(Cnk)
    def combine(self, n: int, k: int) :
        def backtrack(first=1,curr=[]):
            if len(curr)==k:
                output.append(curr[:])
            for i in range(first,n+1):
                curr.append(i)
                backtrack(i+1,curr)
                curr.pop()
        output=[]
        backtrack()
        return output

    #字典序(二进制排序)组合
    def combine1(self, n: int, k: int) :
        nums=[i for i in range(1,n+1)]+[n+1]
        output,j=[],0
        while j<k:
            output.append(nums[:k])
            j=0
            while j<k and nums[j+1]==nums[j]+1:
                nums[j]=j+1
                j+=1
            nums[j]+=1
        return output

if __name__ == '__main__':
    n=4
    k=2
    s=Solution()
    print(s.combine1(n,k))
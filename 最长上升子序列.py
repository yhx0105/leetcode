"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
"""

class Solution:
    #回溯，找到最长的子集
    def lengthOfLIS(self, nums):
        res=[]
        size=len(nums)
        def dfs(tmp,depth,begin):
            if depth==size-1:
                res.append(tmp[:])
                return
            for i in range(begin,size):
                #剪枝条件
                if len(tmp)==0:
                    tmp.append(nums[i])
                else:
                    if tmp[-1]>nums[i+1]:
                        continue
                    tmp.append(nums[i])
                    dfs(tmp,depth+1,begin+1)
                    tmp.pop()
        dfs([],0,0)
        return res

if __name__ == '__main__':
    nums=[10,9,2,5]
    s=Solution()
    print(s.lengthOfLIS(nums))
"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    #回溯+减枝
    def subsetsWithDup(self, nums):
        res=[[]]
        size=len(nums)
        nums=sorted(nums)
        def dfs(nums,path,depth,begin):
            if depth==size:
                return
            for i in range(begin,size):
                if i>begin and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                res.append(path[:])
                dfs(nums,path,depth+1,i+1)
                path.pop()
        dfs(nums,[],0,0)
        return res


if __name__ == '__main__':
    nums=[1,2,2]
    s=Solution()
    print(s.subsetsWithDup(nums))
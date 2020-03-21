"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
"""
class Solution:
    #回溯+剪枝
    def subsets(self, nums):
        res=[]
        size=len(nums)
        used=[False]*size
        def dfs(nums,tmp,used,size,begin):
            if len(tmp)>size:
                return
            for i in range(begin,size):
                if not used[i]:
                    used[i]=True
                    tmp.append(nums[i])
                    res.append(tmp[:])
                    dfs(nums,tmp,used,size,i)
                    used[i]=False
                    tmp.pop()
        dfs(nums,[],used,size,0)
        return res

    def subsets1(self, nums):
        res=[]
        size=len(nums)
        used=[False]*size
        def dfs(nums,tmp,size,begin):
            if len(tmp)>size:
                return
            for i in range(begin,size):
                used[i]=True
                tmp.append(nums[i])
                res.append(tmp[:])
                dfs(nums,tmp,size,i+1)
                tmp.pop()
        dfs(nums,[],size,0)
        return res


if __name__ == '__main__':
    s=Solution()
    nums=[1,2,3]
    print(s.subsets1(nums))
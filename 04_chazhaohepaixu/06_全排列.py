"""
给定一个没有重复数字的序列，返回其所有可能的全排列。
"""
class Solution:
    #有点递归的味道,不断把后面的数前插,
    #怎么表示不同的元素放第一个呢
    #时间复杂度O(n!)
    # def permute(self, nums):
    #     def backtrack(first=0):
    #         if first==n:
    #             output.append(nums[:])
    #         for i in range(first,n):
    #             nums[first],nums[i]=nums[i],nums[first]
    #             backtrack(first+1)
    #             nums[first],nums[i]=nums[i],nums[first]
    #     output=[]
    #     n=len(nums)
    #     backtrack()
    #     return output
    def permute(self,nums):
        def dfs(nums,size,depth,path,used,res):
            if depth==size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    used[i]=True
                    path.append(nums[i])
                    dfs(nums,size,depth+1,path,used,res)
                    used[i]=False
                    path.pop()
        size=len(nums)
        if len(nums)==0:
            return []
        used=[False for _ in range(size)]
        res=[]
        dfs(nums,size,0,[],used,res)
        return res

if __name__ == '__main__':
    res=[1,2,3]
    s=Solution()
    print(s.permute(res))

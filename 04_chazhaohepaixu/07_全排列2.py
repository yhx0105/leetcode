"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。
"""
class Solution:
    #先全排列，再set
    def permuteUnique1(self, nums) :
        def dfs(nums,size,depth,path,used,res):
            if depth==size:
                res.append(path[:])
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
        res1=[]
        for elem in res:
            if elem not in res1:
                res1.append(elem)
            else:
                continue
        return res1
    #全排列，加剪枝
    def permuteUnique2(self, nums):
        def dfs(nums,used,path,depth,size,res):
            if depth==size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                        continue
                    used[i]=True
                    path.append(nums[i])
                    dfs(nums,used,path,depth+1,size,res)
                    used[i]=False
                    path.pop()
        size=len(nums)
        if size==0:
            return []
        nums.sort()
        used=[False]*size
        res=[]
        dfs(nums,used,[],0,size,res)
        return res




if __name__ == '__main__':
    inputs=[1,1,2]
    s=Solution()
    # print(list({}.fromkeys(inputs).keys()))
    print(s.permuteUnique2(inputs))
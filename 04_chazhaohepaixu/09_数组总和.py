"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合
"""
class Solution:
    #回溯+去重，时间O(n**n) 空间O(n**n)
    def combinationSum(self, candidates, target):
        res=[]
        def dps(candidates,target,path):
            if sum(path)==target:
                path=sorted(path)
                res.append(path[:])
                return
            if sum(path)>target:
                return
            for elem in candidates:
                path.append(elem)
                dps(candidates,target,path)
                path.pop()
        dps(candidates,target,[])
        res1=[]
        for elem2 in res:
            if elem2 not in res1:
                res1.append(elem2)
        return res1

    #回溯+减枝，
    def combinationSum1(self, candidates, target):
        res=[]
        def dfs(candidates,target,path,begin,size):
            if target==0:
                res.append(path[:])
                return
            for index in range(begin,size):
                residue=target-candidates[index]
                if residue<0:
                    break
                path.append(candidates[index])
                dfs(candidates,residue,path,index,size)
                path.pop()
        size=len(candidates)
        if size==0:
            return []
        candidates.sort()
        path=[]
        dfs(candidates,target,path,0,size)
        return res

if __name__ == '__main__':
    candidates=[2,3,5]
    s=Solution()
    print(s.combinationSum1(candidates,8))
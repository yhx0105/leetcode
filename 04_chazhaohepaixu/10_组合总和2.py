"""
给定一个数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
"""
class Solution:
    #回溯+剪枝
    def combinationSum2(self, candidates, target):
        res=[]
        candidates=sorted(candidates)
        def dfs(candidates,target,path,begin):
            if target==sum(path):
                res.append(path[:])
                return
            if sum(path)<0:
                return
            for i in range(begin,len(candidates)):
                if i >begin and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(candidates,target,path,i+1)
                path.pop()
        dfs(candidates,target,[],0)
        return res

    def combinationSum3(self, candidates, target):
        res=[]
        size=len(candidates)
        candidates=sorted(candidates)
        def dfs(begin,path,residue):
            if residue==0:
                res.append(path[:])
                return
            for index in range(begin,size):
                if candidates[index]>residue:
                    break
                if index>begin and candidates[index-1]==candidates[index]:
                    continue
                path.append(candidates[index])
                dfs(index+1,path,residue-candidates[index])
                path.pop()
        dfs(0,[],target)
        return res

if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    s = Solution()
    print(s.combinationSum2(candidates, 8))
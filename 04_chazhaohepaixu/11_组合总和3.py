"""
找出所有相加之和为 n 的 k 个数的组合。
组合中只允许含有 1 - 9 的正整数，
并且每种组合中不存在重复的数字。
说明：所有数字都是正整数。
解集不能包含重复的组合。
"""
class Solution:
    #回溯+去重  减枝？？再看
    def combinationSum3(self, k: int, n: int):
        res=[]
        tmp=[i for i in range(1,10)]
        used=[False]*9
        def dps(tmp,depth,curr,used):
            if depth==k:
                if sum(curr)==n:
                    curr=sorted(curr)
                    res.append(curr[:])
                    return
                else:
                    return
            for i,elem in enumerate(tmp):
                if not used[i]:
                    used[i]=True
                    curr.append(elem)
                    dps(tmp,depth+1,curr,used)
                    used[i]=False
                    curr.pop()
        dps(tmp,0,[],used)
        res1=[]
        for elem in res:
            if elem not in res1:
                res1.append(elem)
        return res1

if __name__ == '__main__':
    n=7
    k=3
    s=Solution()
    print(s.combinationSum3(k,n))


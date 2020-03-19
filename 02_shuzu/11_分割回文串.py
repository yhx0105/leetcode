"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案
"""
class Solution:
    #回溯
    def partition(self, s: str):
        res=[]
        def helper(s,tmp):
            if not s:
                res.append(tmp)
            for i in range(1,len(s)+1):
                if s[:i]==s[:i][::-1]:
                    helper(s[i:],tmp+[s[:i]])
        helper(s,[])
        return res
if __name__ == '__main__':
    res='abb'
    s=Solution()
    print(s.partition(res))

"""
给定一个仅包含数字 2-9 的字符串，
返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。
注意 1 不对应任何字母。
"""
import copy
class Solution():
    #暴力法
    # def letterCombinations(self, digits: str) :
    #     dic={'2':'abc','3':'def','4':'ghi',
    #          '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    #     alpha=[]
    #     res=[]
    #     for elem in digits:
    #         alpha.append(dic[elem])
    #     for i in alpha[0]:
    #         res.append(i)
    #     def helper(res, alpha, num):
    #         if num >= len(alpha):
    #             return res
    #         tmp = []
    #         for str1 in res:
    #             for str2 in alpha[num]:
    #                 tmp.append(str1 + str2)
    #         helper(tmp, alpha, num + 1)
    #     return helper(res,alpha,1)
    #暴力法 时间0(3n*4m)  空间O(3n*4m)
    def letterCombinations(self, digits: str):
        dic={'2':'abc','3':'def','4':'ghi',
         '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def backtrack(combination,next_digits):
            if len(next_digits)==0:
                output.append(combination)
            else:
                for letter in dic[next_digits[0]]:
                    backtrack(combination+letter,next_digits[1:])
        output=[]
        if digits:
            backtrack("",digits)
        return output


if __name__ == '__main__':
    input='234'
    s=Solution()
    res=s.letterCombinations(input)
    print(res)


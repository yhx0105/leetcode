"""
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，
序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack_a=[]
        l=len(pushV)
        index=0
        for i in range(l):
            stack_a.append(pushV[i])
            while stack_a[-1]==popV[index]:
                stack_a.pop()
                index=index+1
                if index==l:
                    break
        if stack_a:
            return False
        else:
            return True


if __name__ == '__main__':
    pushV,popV=[1,2,3,4,5],[3,5,4,2,1]
    s=Solution()
    print(s.IsPopOrder(pushV,popV))
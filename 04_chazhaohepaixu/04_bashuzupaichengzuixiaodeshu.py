"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
from functools import cmp_to_key
class Solution:
    #自定义排序规则
    def compare(self,num1,num2):
        t1=str(num1)+str(num2)
        t2=str(num2)+str(num1)
        if t1<t2:
            return -1
        elif t2<t1:
            return 1
        else:
            return 0

    def PrintMinNumber(self, numbers):
        if numbers is None:
            return ""
        lens=len(numbers)
        if lens==0:
            return ""
        tmpNumbers=sorted(numbers,key=cmp_to_key(self.compare))
        return int("".join(str(x)for x in tmpNumbers))

if __name__ == '__main__':
    nums=[1,2,34]
    s=Solution()
    print(s.PrintMinNumber(nums))
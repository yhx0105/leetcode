# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
class Solution:
    #递归
    def jumpFloorII(self, number):
        # write code here
        if number<=-1:
            return False
        elif number<=2:
            return number
        else:
            return 2*self.jumpFloorII(number-1)
# 找规律
    def jumpFloorII2(self, number):
        # write code here
        if number<=-1:
            return False
        elif number<2:
            return number
        else:
            ret=1
            a=1
            for i in range(2,number+1):
                ret=2*a
                a=ret
            return ret

if __name__ == '__main__':
    s=Solution()
    print(s.jumpFloorII2(6))
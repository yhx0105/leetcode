"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
"""
# -*- coding:utf-8 -*-
class Solution:
    #面试官让你回家等通知算法
    def Power(self, base, exponent):
        # write code here
        return base**exponent

    #快速求幂算法
    """
     1.全面考察指数的正负、底数是否为零等情况。 
     2.写出指数的二进制表达，例如13表达为二进制1101。 
     3.举例:10^1101 = 10^0001*10^0100*10^1000。 
     4.通过&1和>>1来逐位读取1101，为1时将该位代表的乘数累乘到最终结果。
    """
    def Power1(self,base,exponent):
        if base==0 :
            return 0
        if exponent==0:
            return 1
        if base==1 or exponent==1:
            return base
        e=abs(exponent)
        res=1
        while e>0:
            if e&1==1:
                res=res*base
            #base翻倍
            base*=base
            e=e>>1
        return res if exponent>0 else 1/res

if __name__ == '__main__':
    s=Solution()
    res=s.Power1(2,-3)
    print(res)


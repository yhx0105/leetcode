"""
输入一个整数，输出该数二进制表示中1的个数。
其中负数用补码表示
"""
# -*- coding:utf-8 -*-
class Solution:
    """
    补码：正数不变，负数是它正数的反码+1
    egg:2的 二进制  1 0000....0010，反码 1 1111....1101
    2的反码加1
    -2的反码 1 1111....1110
    """
    def NumberOf1(self, n):
        # write code here
        n=0xFFFFFFFF&n
        #把所有负数化为正数
        b = bin(n)
        count=0
        for e in b:
            if e=="1":
                count+=1
        return count

#用1（1自身左移运算，其实后来就不是1了）和n的每位进行位与，来判断1的个数
    def NumberOf12(self, n):
        count=0
        for i in range(32):
            mask = 1 << i
            if n&mask !=0:
                count+=1
        return count


if __name__ == '__main__':
    s=Solution()
    print(s.NumberOf12(3))


"""
写一个函数，求两个整数之和，
要求在函数体内不得使用+、-、*、/四则运算符号。
"""
class Solution:
    """
    亦或处理加法，与处理进制，当不进之后，就停止了
    两个数异或：相当于每一位相加，而不考虑进位；
    两个数相与，并左移一位：相当于求得进位；
    将上述两步的结果相加
    """
    #万物皆可递归
    def Add1(self, num1, num2):
        # write code here
        if num1==0:
            return num2
        if num2==0:
            return num1
        return self.Add((num1&num2)<<1,num1^num2)

    #递归改循环,负数会时间超时
    """
    ~A   A的补码按位取反  
    ~1=-2(因为1的补码为0000 0001，按位取反为1111 1110 这个是-2的补码) 
    """
    def Add2(self, num1, num2):
        while num1!=0:
            temp=num1^num2&0xFFFFFFFF
            num1=((num1&num2)<<1)&0xFFFFFFFF
            num2=temp
        return num2 if num2<=0x7FFFFFFF else ~(num2^0xFFFFFFFF)

if __name__ == '__main__':
    s=Solution()
    print(s.Add2(-56,74))
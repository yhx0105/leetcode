"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
class Solution:
    #递归f(n)=f(n-1)+f(n-2)
    def rectCover(self, number):
        # write code here
        if number<=0:
            return 0
        if number<=2:
            return number
        return self.rectCover(number-1)+self.rectCover(number-2)

    #递归改循环
    def rectCover1(self,number):
        if number<0:
            return 0
        if number<=2:
            return number
        a=1
        b=2
        res=0
        while number>2:
            res=a+b
            a=b
            b=res
            number-=1
        return res


if __name__ == '__main__':
    s=Solution()
    print(s.rectCover1(6))

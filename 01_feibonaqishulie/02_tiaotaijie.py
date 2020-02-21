class Solution:
    def jumpFloor1(self, number):
        # write code here
        #递归
        if number<=3:
            return number
        else:
            return self.jumpFloor1(number-1)+self.jumpFloor1(number-2)

        #循环
    def jumpFloor2(self,number):
        if number<=3:
            return number
        else:
            a=1
            b=0
            ret=0
            for i in range(number):
                ret=a+b
                b=a
                a=ret
            return ret

if __name__ == '__main__':
    s=Solution()
    print(s.jumpFloor1(4))
    print(s.jumpFloor2(3))
"""
定义栈的数据结构，
请在该类型中实现一个能够得到栈中所含最小元素的min函数
（时间复杂度应为O（1））。
"""
class Solution:
    def __init__(self):
        #A为住栈，B为辅助栈
        self.A=[]
        self.B=[]
#插入元素在push时比较，最小值
    def push(self, node):
        # write code here
        min_t=self.min()
        if not min_t or min_t>node:
            self.B.append(node)
        else:
            self.B.append(min_t)
        self.A.append(node)

    def pop(self):
        if self.A:
            self.A.pop()
            self.B.pop()

#在pop比较最小值,B不插入比前一元素大的值
    def push2(self,node):
        min_t=self.min()
        if not min_t or node<min_t:
            self.B.append(node)
            self.A.append(node)
        else:
            self.A.append(node)

    def pop2(self):
        if self.A:
            if self.top()>self.min():
                self.A.pop()
            else:
                self.A.pop()
                self.B.pop()


    def top(self):
        # write code here
        if self.A:
            return self.A[-1]

    def min(self):
        # write code here
        if self.B:
            return self.B[-1]

if __name__ == '__main__':
    s=Solution()
    s.push(3)
    print(s.min())

"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)
中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""
# -*- coding:utf-8 -*-
class Solution:
    #字典存储，找到第一个出现一次的字符
    def FirstNotRepeatingChar1(self, s):
        # write code here
        tmpdic={}
        for elem in s:
            if elem not in tmpdic:
                tmpdic[elem]=1
            else:
                tmpdic[elem]+=1
        count=0
        for i in list(tmpdic.values()):
            if i>1:
                count+=i
            else:
                return int(count)
            if count==len(s):
                return -1
    #建立Hash表,ord()函数，返回字母对应的hash值
    def FirstNotRepeatingChar2(self, s):
        ls=[0]*256
        for i in s:
            ls[ord(i)]+=1
        for j in s:
            if ls[ord(j)]==1:
                return s.index(j)
        return -1


if __name__ == '__main__':
    str1='googlle'
    s=Solution()
    # print(s.FirstNotRepeatingChar1(str1))
    nums=[0]*10
    print(nums)
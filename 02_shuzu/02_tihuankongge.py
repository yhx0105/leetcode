# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy
# .则经过替换之后的字符串为We%20Are%20Happy。
class Solution:
    # s 源字符串
    #作弊做法
    def replaceSpace1(self, s):
        # write code here
        new_s=s.replace(' ','%20')
        return new_s

    #从前向后记录" "数目，从后向前替换" "
    def replaceSpace2(self,s):
        #从前先后寻找空格
        l=len(s)
        a=[]
        for i in range(l):
            if s[i]==" ":
                a.append('%20')
            else:
                a.append(s[i])
        return "".join(a)
        #从后往前替换空格




if __name__ == '__main__':
    s="We Are Happy"
    s1=Solution()
    print(s1.replaceSpace2(s))

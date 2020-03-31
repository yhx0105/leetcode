"""
二进制手表顶部有 4 个 LED 代表小时（0-11），
底部的 6 个 LED 代表分钟（0-59）。
每个 LED 代表一个 0 或 1，最低位在右侧。
"""
class Solution:
    def readBinaryWatch(self, num: int):
        tmp=[0]*10
        res=[]
        def dfs(depth,tmp,begin):
            if depth==num:
                res.append(tmp[:])
                return
            for i in range(begin,10):
                tmp[i]=1
                if not self.calc_sum(tmp):
                    tmp[i]=0
                    continue
                dfs(depth+1,tmp,begin+1)
                tmp[i]=0
        dfs(0,tmp,0)
        final_res=self.cal_time(res,[])
        return final_res

#剪纸条件：
    def calc_sum(self,tmp):
        sum_h=0
        sum_m=0
        for i in range(len(tmp)):
            if tmp[i]==0:
                continue
            if i<4:
                sum_h=sum_h+2**(i)
            else:
                sum_m=sum_m+2**(i-4)
        return 0<=sum_h<=11 and 0<=sum_m<=59

    def cal_time(self,res,final_res):
        for elem in res:
            sum_h = 0
            sum_m = 0
            for i in range(len(elem)):
                if i<4:
                    sum_h = sum_h + elem[i]*2 ** (i)
                else:
                    sum_m = sum_m + elem[i]*2 ** (i - 4)
            if sum_m<10:
                sum_m='0'+str(sum_m)
            else:
                sum_m=str(sum_m)
            final_res.append(str(sum_h)+":"+sum_m)
        return final_res


if __name__ == '__main__':
    num=1
    s=Solution()
    res=s.readBinaryWatch(num)
    print(res)

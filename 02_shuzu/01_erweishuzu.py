# 在一个二维数组中（每个一维数组的长度相同），
# 每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，
# 判断数组中是否含有该整数。
class Solution:
    #暴力法
    def Find1(self,target,array):
        for i in range(len(array)):
            for j in range(len(array[0])):
                if target==array[i][j]:
                    return True
        return False

    # array 二维列表
    def Find(self, target, array):
        # write code here
        length=len(array)-1
        width=len(array[0][:])-1
        l=length
        w=0
        if width<0:
            return False
        if target>array[length][width]:
            return False
        elif target==array[length][width]:
            return True
        else:
            while l>=0 and w>=0:
                if target<array[l][w]:
                    l=l-1
                elif target>array[l][w]:
                    w=w+1
                else:
                    return True
            return False



if __name__ == '__main__':
    s=Solution()
    array=[[1,2,8,9],[4,7,10,13]]
    target=7
    print(s.Find(target,array))
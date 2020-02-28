import sys

def isSame(nums):
    new_nums=sorted(nums)
    #判断最后一个数除以前面的数是否为2的倍数
    max_num=new_nums[-1]
    for elem in new_nums:
        while elem<max_num:
            elem=2*elem
        if elem!=max_num:
            return False
    return True

if __name__ == '__main__':
    n=int(sys.stdin.readline().strip())
    l=[]
    for i in range(n):
        line=sys.stdin.readline().strip()
        l.append(int(line))
    print(isSame(l))
    # print(2*2)




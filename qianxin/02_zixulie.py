import sys

def self_sort(nums):
    res=0
    leftP=0
    rightP=1
    l=len(nums)-1
    if l==0:
        return 1
    if l<0:
        return 0
    while rightP<l:
        flag = True
        if nums[leftP]>nums[rightP]:
            while nums[leftP]>nums[rightP] and flag and rightP<l:
                leftP+=1
                rightP=leftP+1
            res+=1
        else:
            flag=False
            while nums[leftP]<nums[rightP] and not flag and rightP<l:
                leftP+=1
                rightP=leftP+1
            res+=1
    return res

if __name__ == '__main__':
    n=int(sys.stdin.readline().strip())
    l=[]
    for line in sys.stdin:
       a=line.split()
    for i in range(n):
        l.append(int(a[i]))
    print(self_sort(l))

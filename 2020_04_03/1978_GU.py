import sys

N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

max_num = max(nums)
#A = [x for x in range(1,max_num+1)]
check = [True] * len(nums)
for k in range(len(nums)):
    if nums[k] == 1:
        check[k] = False
for i in range(2,max_num//2+1):
    j=2
    while(i*j <= max_num):
        for k in range(len(nums)):
            if i*j == nums[k]:
                check[k] = False
        j += 1

print(check.count(True))


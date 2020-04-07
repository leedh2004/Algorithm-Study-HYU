import sys
import copy

N = int(sys.stdin.readline())
d = [0] * 10001
nums = [i for i in range(10,0,-1)]
d[1] = 10
d[2] = 55
before =[]

for i in range(3,N+1):
    before = copy.deepcopy(nums)
    for j in range(10):
        if j==0:
            nums[0] = d[i-1]
        else:
            nums[j] = nums[j-1]-before[j-1]
        d[i] += nums[j]%10007

print(d[N]%10007)

    

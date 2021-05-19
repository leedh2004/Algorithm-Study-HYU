import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
L = list(map(int,input().strip().split()))
L.sort()
result = 0

for i in range(1,N):
    idx = bisect_left(L, L[i]*0.9, lo=0, hi=i-1)
    result += i-idx

print(result)
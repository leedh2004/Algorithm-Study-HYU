import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input(2))
L = list(map(int,input().strip().split()))
L.sort()
result = 0

for j in range(1,N):
    idx = bisect_left(L, L[j]*0.9, lo=0, hi=j)
    result += j-idx

print(result)
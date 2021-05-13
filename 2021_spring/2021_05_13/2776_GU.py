import sys
from bisect import bisect_left

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    A1 = list(map(int, sys.stdin.readline().split()))
    A1.sort()
    M = int(sys.stdin.readline())
    A2 = list(map(int, sys.stdin.readline().split()))
    for i in range(M):
        b =bisect_left(A1,A2[i])
        if b < N and A1[b] == A2[i]:
            print(1)
        else:
            print(0)
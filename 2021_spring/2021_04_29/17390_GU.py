import sys

N, Q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
prefix_sum = [0 for _ in range(N+1)]
prefix_sum[1] = A[0]
for i in range(2, N+1):
    prefix_sum[i] = prefix_sum[i-1] + A[i-1]
for _ in range(Q):
    L, R = map(int, sys.stdin.readline().split())
    print(prefix_sum[R]-prefix_sum[L-1])

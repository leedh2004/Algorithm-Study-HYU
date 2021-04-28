import sys
input = sys.stdin.readline

N, Q = map(int,input().strip().split())
A = sorted(list(map(int, input().strip().split())))
prefix_sum = [0 for _ in range(N+1)]

for i in range(1, N+1, 1):
    prefix_sum[i] = prefix_sum[i-1] + A[i-1]

for _ in range(Q):
    s,e = map(int,input().strip().split())
    print(prefix_sum[e]-prefix_sum[s-1])
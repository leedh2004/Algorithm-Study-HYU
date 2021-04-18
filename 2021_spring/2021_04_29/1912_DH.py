import sys 
N = int(input())
lis = list(map(int, sys.stdin.readline().strip().split()))
lis = [0] + lis 
dp = [0 for _ in range(N+1)]
ret = -10000
for i in range(1, N+1):
    dp[i] = dp[i-1] + lis[i] if dp[i-1] > 0 else lis[i]
    ret = max(ret, dp[i])
print(ret)

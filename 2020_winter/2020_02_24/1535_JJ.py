import sys

# 입력
n = int(sys.stdin.readline())
loss = list(map(int,sys.stdin.readline().split()))
get = list(map(int,sys.stdin.readline().split()))

# dp
dp = [0 for _ in range(101)]

# 배낭 알고리즘
for i in range(n):
  for j in range(100,loss[i],-1):
    dp[j] = max(dp[j],dp[j-loss[i]]+get[i])

print(dp[100])

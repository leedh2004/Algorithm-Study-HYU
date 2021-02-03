import sys

dp = [[ 0 for col in range(4)] for row in range(100001)]

dp[1][1] = 1 # 1 = 1
dp[2][2] = 1 # 2 = 2
dp[3][1] = 1 # 3 = 2 + 1
dp[3][2] = 1 # 3 = 1 + 2
dp[3][3] = 1 # 3 = 3

m = 1000000009

for i in range(4,10):
  for j in range(1,4):
    if j==1:
      dp[i][j] = (dp[i-1][2] + dp[i-1][3]) % m
    elif j==2:
      dp[i][j] = (dp[i-2][1] + dp[i-2][3]) % m
    elif j==3:
      dp[i][j] = (dp[i-3][1] + dp[i-3][2]) % m

t = int(sys.stdin.readline())
for i in range(t):
  n = int(sys.stdin.readline())
  print( (dp[n][1] + dp[n][2] + dp[n][3]) % m)
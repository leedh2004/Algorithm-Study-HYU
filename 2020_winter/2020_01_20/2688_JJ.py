import sys

dp = [[ 0 for col in range(10)] for row in range(65)]
dp[0][0] = 1

for i in range(1,65):
  for j in range(0,10):

    if j==0:
      dp[i][j] = 1

    else :
      tmp = 0
      for k in range(0,j+1):
        tmp = tmp + dp[i-1][k]
      dp[i][j] = tmp

t = int(sys.stdin.readline())
for i in range(t):
  n = int(sys.stdin.readline())
  print(sum(dp[n]))
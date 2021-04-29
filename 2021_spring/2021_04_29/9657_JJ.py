import sys

input = sys.stdin.readline

n = int(input())
dp = [False for _ in range(1000)]
dp[0],dp[2],dp[3] = True,True,True

for idx in range(4,n):
  dp[idx] = not(dp[idx-1] and dp[idx-3] and dp[idx-4])

if dp[n-1]:
  print('SK')
else :
  print('CY')


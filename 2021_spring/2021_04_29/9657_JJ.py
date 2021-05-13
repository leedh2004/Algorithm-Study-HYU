import sys

input = sys.stdin.readline

n = int(input())

# 상근이 이길때 - True
# 창영이 이길때 - False

dp = [False for _ in range(1000)]
dp[0],dp[2],dp[3] = True,True,True

for idx in range(4,n):
  # -1,-3,-4 에서 A가 모두 이겼다면 이제는 B가 이김
  dp[idx] = not(dp[idx-1] and dp[idx-3] and dp[idx-4])

if dp[n-1]:
  print('SK')
else :
  print('CY')


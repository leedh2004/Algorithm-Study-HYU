import sys
import math
input = sys.stdin.readline

h,y = map(int,input().split())
dp = [0 for _ in range(y+1)]
dp[0] = h
val = [1,3,5]
money = [1.05,1.2,1.35]
for i in range(1,y+1):
  for j in range(3):
    if i - val[j] >=0:
      dp[i] = max(dp[i], math.floor(dp[i - val[j]]*money[j] ))

print(max(dp))

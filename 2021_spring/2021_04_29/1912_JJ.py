import sys

imput = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = arr[:]

for idx in range(1,n):
  dp[idx]=  max(dp[idx],dp[idx-1]+arr[idx])

print(max(dp))
import sys

#입력
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

#dp테이블 생성 
dp = [1 for _ in range(n)]
ans = 1

#LIS
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j]+1
            ans = max(ans,dp[i])

print(ans)

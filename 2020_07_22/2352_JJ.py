n = int(input())
dp = [1 for i_ in range(n)]

#가중치 입력
value = list(map(int,input().split()))

#LIS
for i in range(n):
    for j in range(i):
        if value[i]>=value[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(max(dp))

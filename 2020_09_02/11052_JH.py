N = int(input())
P = list(map(int,input().split()))
P.insert(0,0)
dp = [ 0 for _ in range(N+1)]
dp[1] = P[1]

for i in range(2, N+1, 1):
    dp[i] = P[i]
    for j in range(i, 0, -1):
        if dp[i] < dp[j]+P[i-j]:
            dp[i] = dp[j] + P[i-j]

print(dp[N])
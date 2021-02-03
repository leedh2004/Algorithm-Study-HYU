T = int(input())
dp = [0 for _ in range(100)]
dp[0], dp[1], dp[2] = 1,1,1

for i in range(3,100,1):
    dp[i] = dp[i-3] + dp[i-2]

for i in range(T):
    index = int(input())
    print(dp[index-1])
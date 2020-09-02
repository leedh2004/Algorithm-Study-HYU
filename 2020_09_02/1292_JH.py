dp = [0 for _ in range(1001)]
dp[1] = 1
tmp = 2
count = 0
for i in range(2, 1001, 1):
    dp[i] = dp[i-1]+tmp
    count += 1
    if tmp == count :
        tmp += 1
        count = 0

a,b = map(int,input().split())
print(dp[b]-dp[a-1])
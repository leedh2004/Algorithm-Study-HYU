N = int(input())
box = list(map(int,input().split()))
dp = [ 1 for _ in range(N) ]

for i in range(N):
    for j in range(i):
        if(box[j]<box[i] and dp[j]+1>dp[i]):
            dp[i] = dp[j]+1

print(max(dp))
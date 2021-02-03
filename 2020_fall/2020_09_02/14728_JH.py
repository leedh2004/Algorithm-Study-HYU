N,T = map(int,input().split())
w = [ 0 for _ in range(N+1)]
v = [ 0 for _ in range(N+1)]
dp = [ [0 for _ in range(T+1)] for i in range(N+1)]
result = 0
for i in range(N):
    w[i+1],v[i+1] = map(int,input().split())
for i in range(1, N+1, 1):
    for j in range(1,T+1,1):
        if w[i] <= j :
            dp[i][j] = max(v[i]+dp[i-1][j-w[i]],dp[i-1][j]) 
        else :
            dp[i][j] = dp[i-1][j]
        result = max(result, dp[i][j])

print(result)
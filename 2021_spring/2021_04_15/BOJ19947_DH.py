H, Y = map(int, input().split())

dp = [ 0 for _ in range(Y+1) ]
dp[0] = H

def f(dp, n):
    if n < 0:
        return -1
    elif dp[n] != 0:
        return dp[n]
    dp[n] = int(max(1.05 * f(dp, n-1), 1.2 * f(dp, n-3), 1.35 * f(dp, n-5)))
    return dp[n]

print(f(dp, Y))

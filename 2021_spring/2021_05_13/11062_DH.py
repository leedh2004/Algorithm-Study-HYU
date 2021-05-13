T = int(input())
def solve(turn, i, j):
    global dp, C
    if i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if turn:
        dp[i][j] = max(solve(False, i+1, j) + C[i], solve(False, i, j-1) + C[j])
        return dp[i][j]
    else:
        dp[i][j] = min(solve(True, i+1, j), solve(True, i, j-1))
        return dp[i][j]

for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    dp = [ [-1 for _ in range(N)] for _ in range(N)]
    print(solve(True, 0, N-1))
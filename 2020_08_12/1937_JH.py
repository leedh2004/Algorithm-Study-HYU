def dfs(x,y):
    global n,mat,dp,dx,dy
    if dp[x][y] != 0:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if(nx>=0 and nx<n and ny>=0 and ny<n and mat[nx][ny]>mat[x][y]):
            dp[x][y] = max(dp[x][y],dfs(nx,ny)+1)
    return dp[x][y]

n = int(input())
mat = [ list(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = -1

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i,j))

print(result)
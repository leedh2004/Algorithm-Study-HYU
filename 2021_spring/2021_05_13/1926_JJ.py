import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def is_in(x,y):
    return 0<=x<n and 0<=y<m

def dfs(x,y):
    # print('dfs',x,y)
    visited[x][y] = True
    ret = 1
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if is_in(nx,ny) and not visited[nx][ny] and table[nx][ny]:
            ret = ret + dfs(nx,ny)
    return ret

n,m = map(int,input().split())
table = []
for _ in range(n):
    table.append(list(map(int,input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]

num = 0
ans = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and table[i][j]:
            num = num + 1
            ans = max(ans,dfs(i,j))
print(num)
print(ans)

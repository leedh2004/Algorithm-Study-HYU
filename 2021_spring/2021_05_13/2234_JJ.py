import sys
from collections import defaultdict

input = sys.stdin.readline

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def is_in(x,y):
    return 0<=x<m and 0<=y<n

def dfs(x,y,idx):
    visited[x][y] = True
    numTable[x][y] = idx
    val = table[x][y]
    ret = 1
    for i in range(4):
        num = 3-i
        check = 2**num

        # 벽에 막힌 경우
        if val >= check:
            val = val - check
            nx,ny = x+dx[i], y+dy[i]
            # 인접 목록 구하기
            if is_in(nx,ny) :
                adjPoints[idx].append((nx,ny))
            continue
        # 막히지 않은 경우 -> 탐색
        else :
            nx,ny = x+dx[i], y+dy[i]
            if is_in(nx,ny) and not visited[nx][ny]:
                ret = ret + dfs(nx,ny,idx)
    return ret

n,m = map(int,input().split())
table = []
for i in range(m):
    table.append(list(map(int,input().split())))



numTable = [[0 for _ in range(n)] for _ in range(m)]
sizes = []
adjPoints = defaultdict(list)
visited = [[False for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            # 각자 크기 저장
            size = dfs(i,j,len(sizes))
            sizes.append(size)

adj = defaultdict(dict)
for i in range(len(sizes)):
    for j in range(len(adjPoints[i])):
        adjx,adjy = adjPoints[i][j]
        adjIndex = numTable[adjx][adjy]
        if i!= adjIndex:
            adj[i][adjIndex] = True

ans = 0
for i in range(len(sizes)):
    for j in adj[i].keys():
        ans = max(ans, sizes[i]+sizes[j])

print(len(sizes))
print(max(sizes))
print(ans)
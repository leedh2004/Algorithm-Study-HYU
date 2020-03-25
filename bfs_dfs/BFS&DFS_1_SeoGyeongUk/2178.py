import sys

def inRange(y,x):
    return (y>=0 and y<=N-1) and (x>=0 and x<=M-1)

def bfs():
    q = [[0,0]]
    visited[0][0] = True
    dist = [[0]*(M) for _ in range(N)]
    dist[0][0] =1
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]
    while q:
        [y,x] = q.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if(inRange(ny,nx) and visited[ny][nx] == False and maze[ny][nx] != 0):
                visited[ny][nx] = True
                dist[ny][nx] = dist[y][x]+1
                q.append([ny,nx])
    
    return dist[N-1][M-1]



N,M = map(int,sys.stdin.readline().split())
maze =[[0]*(M) for _ in range(N)]
for i in range(N):
    line = list(sys.stdin.readline())
    for j in range(M):
        if(line[j]=='1'):
            maze[i][j]=1
visited = [[False]*(M) for _ in range(N)]

print(bfs())

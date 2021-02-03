import collections

def bfs(a,b):
    global visit, N, mat
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = collections.deque()
    q.append([a,b])
    visit[a][b] = True
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N and visit[nx][ny] == False and mat[nx][ny] == mat[x][y] :
                q.append([nx,ny])
                visit[nx][ny] = True

N = int(input())
mat = [list(input()) for _ in range(N)]
visit = [[False for _ in range(N)] for i in range(N)]
result, result2 = 0, 0

for i in range(N):
    for j in range(N):
        if visit[i][j] == False :
            result += 1
            bfs(i,j)

visit = [[False for _ in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if mat[i][j] == 'G':
            mat[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if visit[i][j] == False :
            result2 += 1
            bfs(i,j)

print(result, result2)
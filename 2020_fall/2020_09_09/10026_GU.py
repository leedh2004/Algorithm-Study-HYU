import sys
import copy
def inRange(x,y):
    return ((x>=0) and (x<N) and (y>=0) and (y<N))

def bfs(x,y,color,grid):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    q = [[x,y]]
    check[x][y] = True
    while q:
        x,y = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if inRange(nx,ny):
                if not check[nx][ny] and grid[nx][ny]==color:
                    check[nx][ny] = True
                    q.append([nx,ny])

def bfs2(x,y,color,grid):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    q = [[x,y]]
    check2[x][y] = True
    while q:
        x,y = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if inRange(nx,ny):
                if not check2[nx][ny] and grid[nx][ny]==color:
                    check2[nx][ny] = True
                    q.append([nx,ny])

N = int(sys.stdin.readline())
grid1 = [[0] * N for _ in range(N)]
grid2 = [[0] * N for _ in range(N)]
check = [[False] * N for _ in range(N)]
check2 = [[False] * N for _ in range(N)]

for i in range(N):
    grid1[i] = list(sys.stdin.readline().rstrip())
    #이거 안써주고 grid2[i] = grid1[i] 쓰니깐 값 이상하게 나옴
    #이차원 배열이므로 신경써야함
    grid2[i] = copy.deepcopy(grid1[i])
    for j in range(N):
        if grid2[i][j] == 'G': grid2[i][j] = 'R'
cnt1 = 0
for i in range(N):
    for j in range(N):
        if not check[i][j]:
            color = grid1[i][j]
            bfs(i,j,color,grid1)
            cnt1 += 1
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not check2[i][j]:
            color = grid2[i][j]
            bfs2(i,j,color,grid2)
            cnt2 += 1

print(cnt1,cnt2)


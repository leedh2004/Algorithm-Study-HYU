import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().strip().split())
mat = [ list(map(int,input().strip().split())) for _ in range(N) ]
visit = [ [False for _ in range(M)] for i in range(N) ]
count, max_space = 0,0

def is_in(nx,ny):
    global N,M 
    return 0<=nx<N and 0<=ny<M

def bfs(start_x, start_y):
    global visit, mat
    q = deque()
    q.append([start_x, start_y])
    visit[start_x][start_y] = True
    direction = [ [1,0], [-1,0], [0,1], [0,-1] ]
    space = 0

    while q :
        x,y = q.popleft()
        space += 1
        for dx,dy in direction :
            nx,ny = x+dx, y+dy
            if is_in(nx,ny) and not visit[nx][ny] and mat[nx][ny] == 1 :
                q.append([nx,ny])
                visit[nx][ny] = True

    return space

for i in range(N):
    for j in range(M):
        if not visit[i][j] and mat[i][j] == 1 :
            count += 1
            max_space = max(max_space, bfs(i,j))

print(count)
print(max_space)


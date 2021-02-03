import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())
mat = [ list(input().strip()) for _ in range(R) ]
visit = [[False for _ in range(C)] for i in range(R)]
wolf, sheep = 0, 0

def bfs(start_x, start_y):
    global mat, R, C, visit, wolf, sheep
    dx,dy = [1,-1,0,0], [0,0,1,-1]
    q = deque()
    q.append([start_x, start_y])
    visit[start_x][start_y] = True
    tmp_wolf, tmp_sheep = 0,0

    while q :
        for i in range(len(q)):
            x,y = q.popleft()
            if mat[x][y] == 'v':
                tmp_wolf += 1
            if mat[x][y] == 'k':
                tmp_sheep += 1
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if nx>=0 and nx<R and ny>=0 and ny<C and mat[nx][ny] != '#' and visit[nx][ny] == False:
                    q.append([nx,ny])
                    visit[nx][ny] = True

                    
    if tmp_wolf >= tmp_sheep :
        wolf += tmp_wolf
    elif tmp_sheep > tmp_wolf :
        sheep += tmp_sheep

for i in range(R):
    for j in range(C):
        if (mat[i][j] == 'v' or mat[i][j] == 'k') and visit[i][j] == False:
            bfs(i,j)

print(sheep,wolf)
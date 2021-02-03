import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    H,W = map(int,input().split())
    mat = [ list(input().strip()) for _ in range(H) ]
    visit = [ [False for _ in range(W)] for i in range(H) ]
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    result = 0

    def bfs(start_x, start_y):
        global H,W,mat,visit, dx,dy
        q = deque()
        q.append([start_x, start_y])
        visit[start_x][start_y] = True

        while q :
            for i in range(len(q)):
                x,y = q.popleft()
                for i in range(4):
                    nx,ny = x+dx[i], y+dy[i]
                    if nx>=0 and nx<H and ny>=0 and ny<W and mat[nx][ny] == '#' and visit[nx][ny] == False :
                        q.append([nx,ny])
                        visit[nx][ny] = True


    for i in range(H):
        for j in range(W):
            if mat[i][j] == '#' and visit[i][j] == False :
                bfs(i,j)
                result += 1

    print(result)
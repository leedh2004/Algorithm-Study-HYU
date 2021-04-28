import sys
input = sys.stdin.readline
from copy import deepcopy
from collections import deque

N,L,R = map(int,input().strip().split())
mat = [list(map(int,input().strip().split())) for _ in range(N)]
result = 0
dx,dy = [-1,1,0,0], [0,0,-1,1]

def is_in(x,y):
    global N

    if 0<=x<N and 0<=y<N :
        return True
    return False


def diff(x,y,nx,ny) :
    return abs(mat[x][y]-mat[nx][ny])

def is_diff(x,y) :
    global dx, dy, L, R

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if is_in(nx,ny) and L<=diff(x,y,nx,ny)<=R :
            return True
    return False


def bfs(x,y, visit, tmp_mat):
    global mat, dx, dy
    q = deque([[x,y]])
    area = []
    num_people, num_area = 0,0
    visit[x][y] = True

    while q :
        x,y = q.popleft()
        area.append([x,y])
        num_people += mat[x][y]
        num_area += 1
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if is_in(nx,ny) and visit[nx][ny] == False and L<=diff(x,y,nx,ny)<=R : 
                q.append([nx,ny])
                visit[nx][ny] = True

    num_people = int(num_people/num_area)

    for (x,y) in area :
        tmp_mat[x][y] = num_people
    

while True :
    visit = [[False for _ in range(N)] for i in range(N)]
    tmp_mat = deepcopy(mat)
    flag = True
    for i in range(N):
        for j in range(N):
            if visit[i][j] == False and is_diff(i,j):
                bfs(i,j, visit, tmp_mat)
                flag = False
            visit[i][j] = True

    if flag :
        break
    result += 1
    mat = tmp_mat

print(result)
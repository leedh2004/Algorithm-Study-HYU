import sys
from collections import deque
import copy
input = sys.stdin.readline

N,M = map(int,input().split())
mat = [ list(map(int,input().split())) for _ in range(N) ]
dx,dy = [1,-1,0,0], [0,0,1,-1]
flag = True
time = 0

def bfs(start_x, start_y):
    global N,M, mat, visit, dx,dy
    q = deque()
    q.append([start_x, start_y])
    visit[start_x][start_y] = True

    while q :
        for i in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<M and visit[nx][ny] == False and mat[nx][ny] > 0 :
                    q.append([nx,ny])
                    visit[nx][ny] = True

def aging():
    global N,M,mat, flag, dx, dy, time

    tmp_flag = False
    tmp_mat = copy.deepcopy(mat)

    for i in range(N):
        for j in range(M):
            if mat[i][j] > 0 :
                tmp_count = 0
                for k in range(4):
                    nx,ny = i+dx[k], j+dy[k]
                    if 0<=nx<N and 0<=ny<M and mat[nx][ny] == 0 :
                        tmp_count += 1
                tmp_result = tmp_mat[i][j] - tmp_count
                if tmp_result >= 0 :
                    tmp_mat[i][j] = tmp_result
                else :
                    tmp_mat[i][j] = 0
                tmp_flag = True

    if tmp_flag == True :
        time += 1
        mat = copy.deepcopy(tmp_mat)

    flag = tmp_flag


while flag :
    visit = [ [False for _ in range(M)] for i in range(N) ]
    count = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] > 0 and visit[i][j] == False :
                count += 1
                bfs(i,j)

    if count >= 2 :
        print(time)
        break
    
    aging()

if flag == False :
    print(0)
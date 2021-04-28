import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
mat = [ list(map(int,input().strip().split())) for _ in range(N) ]
time = 0
before_count = sum(mat[i].count(1) for i in range(N))
now_count = before_count
dx,dy = [1,-1,0,0], [0,0,1,-1]

def is_in(x,y):
    global N,M
    return 0<=x<N and 0<=y<M


def bfs(start_x,start_y):
    global N, M, mat, now_count
    
    visit = [[False for _ in range(M)] for i in range(N)]
    q = deque()
    q.append([start_x,start_y])
    visit[start_x][start_y] = True
    tmp_mat = deepcopy(mat)
    count = 0

    while q :
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if is_in(nx,ny) and visit[nx][ny] == False :
                if  mat[nx][ny] == 1 :
                    count += 1
                    tmp_mat[nx][ny] = 0
                else :
                    q.append([nx,ny])
                visit[nx][ny] = True

    mat = tmp_mat
    now_count = count


while now_count :
    before_count = now_count
    time += 1
    bfs(0,0)

if time != 0 :
    time -= 1

print(time)
print(before_count)


# import sys
# input = sys.stdin.readline
# import numpy as np
# from collections import deque
# from copy import deepcopy

# N, M = map(int, input().split())
# mat = [ list(map(int,input().strip().split())) for _ in range(N) ]
# time = 0
# before_count = sum(mat[i].count(1) for i in range(N))
# now_count = before_count
# dx,dy = [1,-1,0,0], [0,0,1,-1]

# def is_in(x,y):
#     global N,M
#     return 0<=x<N and 0<=y<M


# def bfs(start_x,start_y, visit):
#     global N, M, mat, now_count
#     q = deque()
#     q.append([start_x,start_y])
#     visit[start_x][start_y] = True
#     tmp_mat = deepcopy(mat)
#     count = 0
#     flag = False

#     while q :
#         x,y = q.popleft()
#         for i in range(4):
#             nx,ny = x+dx[i], y+dy[i]
#             if is_in(nx,ny) :
#                 if visit[nx][ny] == False :
#                     if  mat[nx][ny] == 1 :
#                         count += 1
#                         tmp_mat[nx][ny] = 0
#                     else :
#                         q.append([nx,ny])
#                     visit[nx][ny] = True

#             else :
#                 flag = True

#     if flag :
#         mat = tmp_mat
#         now_count = count
    
#     return flag


# class TmpError(Exception):
#     def __init__(self):
#         super().__init__('치즈를 녹였음')

# while now_count :
#     print(time, np.array(mat))
#     before_count = now_count

#     visit = [[False for _ in range(M)] for i in range(N)]

#     try :
#         for i in range(N):
#             for j in range(M):
#                 if visit[i][j] == False and mat[i][j] == -1 or mat[i][j] == 0 :
#                     if bfs(i,j, visit) :
#                         raise TmpError
#     except TmpError :
#         time += 1
#         continue


# print(time)
# print(before_count)
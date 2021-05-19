import sys
input = sys.stdin.readline
from copy import deepcopy

N,M,T = map(int,input().strip().split())
mat = [ list(map(int,input().strip().split())) for _ in range(N) ]
cleaner = []

def is_in(x,y):
    global N,M, cleaner
    if 0<=x<N and 0<=y<M and [x,y] not in cleaner :
        return True
    else :
        return False

def diffusion():
    global N, M, mat, cleaner

    tmp_mat = [[0 for _ in range(M)] for i in range(N)]
    d = [ [1,0],[-1,0],[0,1],[0,-1] ]

    for i in range(N):
        for j in range(M):
            if mat[i][j] != 0 and mat[i][j] != -1 :
                count = 0
                value = int(mat[i][j]/5)
                for dx,dy in d :
                    nx,ny = i+dx, j+dy
                    if is_in(nx,ny) :
                        count += 1
                        tmp_mat[nx][ny] += value
                tmp_mat[i][j] += mat[i][j] - value*count

    for x,y in cleaner :
        tmp_mat[x][y] = -1

    return tmp_mat

def clean():
    global N, M, cleaner, mat
    up_x, up_y = cleaner[0][0], cleaner[0][1]
    down_x, down_y = cleaner[1][0], cleaner[1][1]

    # tmp_mat = [ [0 for _ in range(M)] for i in range(N) ]
    tmp_mat = deepcopy(mat)

    for i in range(1,up_x,1):   # | 왼쪽
        tmp_mat[i][0] = mat[i-1][0]
    for i in range(2, M, 1):  # _ 아래
        tmp_mat[up_x][i] = mat[up_x][i-1]
    for i in range(up_x-1,-1,-1): # | 오른쪽
        tmp_mat[i][M-1] = mat[i+1][M-1]
    for i in range(M-2, -1, -1): # - 위
        tmp_mat[0][i] = mat[0][i+1]

    for i in range(N-2,down_x,-1):   # | 왼쪽
        tmp_mat[i][0] = mat[i+1][0]
    for i in range(M-2, -1, -1):  # _ 아래
        tmp_mat[N-1][i] = mat[N-1][i+1]
    for i in range(down_x+1,N,1): # | 오른쪽
        tmp_mat[i][M-1] = mat[i-1][M-1]
    for i in range(2, M, 1): # - 위
        tmp_mat[down_x][i] = mat[down_x][i-1]

    tmp_mat[up_x][up_y] = -1
    tmp_mat[down_x][down_y] = -1
    tmp_mat[up_x][1] = 0
    tmp_mat[down_x][1] = 0


    return tmp_mat

for i in range(N):
    for j in range(M):
        if mat[i][j] == -1 :
            cleaner.append([i,j])

for _ in range(T):
    mat = diffusion()
    # print(mat)
    mat = clean()
    # print(mat)

result = 0
for i in range(N):
    for j in range(M):
        if mat[i][j]!=-1 :
            result += mat[i][j]

print(result)

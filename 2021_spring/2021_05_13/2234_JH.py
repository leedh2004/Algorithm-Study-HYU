import sys
input = sys.stdin.readline
from collections import deque

def is_in(x,y):
    global N, M
    return 0<=x<N and 0<=y<M

def bfs(i,j,now_nat):
    global N, M, mat, nat, D, P
    q = deque()
    q.append([i,j])
    nat[i][j] = now_nat
    ret = 1

    while q :
        x,y = q.popleft()
        CAN_GO = bin(P&mat[x][y])
        flag = True
        for i in range(4) :
            if flag and CAN_GO[-1-i] == 'b' :
                flag = False
            if flag and CAN_GO[-1-i] == '1' :
                continue
            nx,ny = x+D[i][0], y+D[i][1]
            if is_in(nx,ny) and nat[nx][ny] == -1 :
                nat[nx][ny] = now_nat
                q.append([nx,ny])
                ret += 1

    # exit()

    return ret

M, N = map(int,input().strip().split())
mat = [ list(map(int,input().strip().split())) for _ in range(N) ]
# D = [ [1,0], [0,1], [-1,0], [0,-1] ]
D = [ [0,-1], [-1,0], [0,1], [1,0] ]
nat, nat_num = [ [-1 for _ in range(M)] for i in range(N) ], 0
result1, result2, result3 = 0,0,0
P = 15
region = dict()

for i in range(N) : 
    for j in range(M) :
        if nat[i][j] == -1 :
            result1 += 1
            tmp = bfs(i,j, nat_num)
            region[nat_num] = tmp
            result2 = max(result2, tmp)
            nat_num += 1

for i in range(N):
    for j in range(M):
        CAN_GO = bin(P&mat[i][j])
        flag = True
        for k in range(4) :
            if flag and CAN_GO[-1-k] == 'b' :
                flag = False
            if flag and CAN_GO[-1-k] == '0' :
                continue
            ni,nj = i+D[k][0], j+D[k][1]
            if is_in(ni,nj) and nat[i][j] != nat[ni][nj] :
                result3 = max(result3, region[nat[i][j]]+region[nat[ni][nj]] )

# print(nat, region)

print(result1)
print(result2)
print(result3)

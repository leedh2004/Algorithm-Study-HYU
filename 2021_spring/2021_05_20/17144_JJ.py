import sys
from copy import deepcopy

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def is_in(x,y):
    return 0<=x<R and 0<=y<C;

def spread():
    newTable = [ [0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if table[i][j]>0:
                val = 0

                # 확산된 방향 갯수 구하기
                for k in range(4):
                    vx,vy = i+dx[k],j+dy[k]
                    if is_in(vx,vy) and table[vx][vy] !=-1:
                        val = val + 1
                
              
                for k in range(4):
                    nx,ny = i+dx[k],j+dy[k]
                    if is_in(nx,ny) and table[nx][ny] !=-1:
                        newTable[nx][ny] = newTable[nx][ny] + int(table[i][j]/5)

                newTable[i][j] = newTable[i][j] + (table[i][j] - int(table[i][j]/5)*val)

    newTable[machine][0]=-1
    newTable[machine+1][0]=-1
    return newTable

def aircleaner(up, down):

    # 왼쪽 모서리
    for i in range(up-2,-1,-1):
        table[i+1][0] = table[i][0]
    for i in range(down+2,R):
        table[i-1][0] = table[i][0]

    # 위 아래 모서리
    for i in range(1,C):
        table[0][i-1] = table[0][i]
        table[R-1][i-1] = table[R-1][i]

    # 오른쪽 모서리
    for i in range(1,up+1):
        table[i-1][C-1] = table[i][C-1]

    for i in range(R-2,down-1,-1):
        table[i+1][C-1] = table[i][C-1]

    # 가운데처리
    for i in range(C-2,0,-1):
        table[up][i+1] = table[up][i]
        table[down][i+1] = table[down][i]

    table[up][1] = 0
    table[down][1] = 0

def sumTable():
    ret = 0 
    for i in range(R):
        ret = ret + sum(table[i])
    return ret + 2

def printTable():
    for i in range(R):
        print(table[i])


# 입력
R, C, T = map(int,input().split())
table = []
for i in range(R):
    table.append(list(map(int,input().split())))


machine = 0
# 공기청정기 위치 파악
for i in range(R):
    if table[i][0]==-1:
        machine = i
        break

for _ in range(T):
    table = spread()
    aircleaner(machine,machine+1)
print(sumTable())

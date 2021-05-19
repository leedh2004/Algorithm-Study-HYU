import sys
from copy import deepcopy


def inRange(y, x):
    return (0 <= y < R) and (0 <= x < C)


def spread(y, x):
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    dust = grid[y][x]
    s_dust = grid[y][x]//5
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if inRange(ny, nx) and grid[ny][nx] != -1:
            grid2[ny][nx] += s_dust
            dust -= s_dust
    grid2[y][x] += dust


R, C, T = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
air1, air2 = -1, -1
for i in range(2, R):
    if grid[i][0] == -1:
        air1 = i
        air2 = i+1
        break
for _ in range(T):
    grid2 = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] > 0:
                spread(i, j)

    grid3 = [[0 for _ in range(C)] for _ in range(R)]

    # 오른아래, 오른위
    tmp = grid2[air1][C-1]
    tmp2 = grid2[air2][C-1]

    for j in range(1, C-1):
        grid3[air1][j+1] = grid2[air1][j]
        grid3[air2][j+1] = grid2[air2][j]
    grid3[air1][1] = 0
    grid3[air2][1] = 0

    # 오른 위
    tmp3 = grid2[0][C-1]
    for i in range(air1-2, -1, -1):
        grid3[i][C-1] = grid2[i+1][C-1]
    grid3[air1-1][C-1] = tmp

    # 오른 아래
    tmp4 = grid2[R-1][C-1]
    for i in range(air2+2, R):
        grid3[i][C-1] = grid2[i-1][C-1]
    grid3[air2+1][C-1] = tmp2

    # 왼 위, 왼 아래
    tmp5 = grid2[0][0]
    tmp6 = grid2[R-1][0]
    for j in range(C-3, -1, -1):
        grid3[0][j] = grid2[0][j+1]
        grid3[R-1][j] = grid2[R-1][j+1]
    grid3[0][C-2] = tmp3
    grid3[R-1][C-2] = tmp4

    for i in range(2, air1):
        grid3[i][0] = grid2[i-1][0]
    grid3[1][0] = tmp5

    for i in range(R-3, air2, -1):
        grid3[i][0] = grid2[i+1][0]
    grid3[R-2][0] = tmp6

    grid3[air1][0] = -1
    grid3[air2][0] = -1

    for i in range(1, R-1):
        for j in range(1, C-1):
            if i != air1 and i != air2:
                grid3[i][j] = grid2[i][j]

    grid = deepcopy(grid3)

res = sum(sum(grid[i]) for i in range(R))
# 미세먼지 -2
print(res+2)

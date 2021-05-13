import sys
from math import sqrt

N = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt =0
while True:
    cnt += 1
    grid2 = []
    for i in range(0, len(grid), 2):
        for j in range(0, len(grid), 2):
            tmp = [grid[i][j], grid[i+1][j], grid[i][j+1], grid[i+1][j+1]]
            tmp.sort()
            grid2.append(tmp[2])
    if len(grid2) == 1:
       print(grid2[0])
       break
    grid = [grid2[i:i+int(sqrt(len(grid2)))]
            for i in range(0, len(grid2), int(sqrt(len(grid2))))]

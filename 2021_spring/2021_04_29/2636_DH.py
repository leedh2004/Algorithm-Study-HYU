import sys
sys.setrecursionlimit(10**6)

Y, X = map(int, sys.stdin.readline().strip().split())
board = []
for _ in range (Y):
    t = list(map(int, sys.stdin.readline().strip().split()))
    board.append(t)

D = [(0,1), (0, -1), (1, 0), (-1,0)]

def dfs(y, x):
    global Y, X, visited
    if visited[y][x]:
        return
    visited[y][x] = 1
    if board[y][x] == 1:
        board[y][x] = 0
        return
    for i in range(4):
        ny, nx = y + D[i][0], x + D[i][1]
        if 0 <= ny < Y and 0 <= nx < X:
            dfs(ny, nx)

day = 0
ret = 0

while True:
    visited = [ [0] * X for _ in range(Y) ]
    cnt = sum([board[i].count(1) for i in range(Y)])
    dfs(0, 0)
    if cnt == 0:
        break
    else:
        ret = cnt 
    day += 1 
    
print(day)
print(ret)

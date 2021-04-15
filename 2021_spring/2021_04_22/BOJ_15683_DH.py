import copy
from collections import deque

N, M = map(int, input().split())
board = []

# direction
# 0 은 위, 1 오른쪽, 2 아래, 3 왼쪽
D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def move(y, x, direction, board):
    global N, M, D
    ny, nx = y + D[direction][0], x + D[direction][1]
    if ny >= N or nx >= M or ny < 0 or nx < 0:
        return
    if board[ny][nx] == 6:
        return
    board[ny][nx] = -1
    move(ny, nx, direction, board) 
# CASE
C = [ -1, 
[[0], [1], [2], [3]], 
[[0, 2], [1, 3]], 
[[0, 1], [1, 2], [2, 3], [3, 0]], 
[[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 
[[0, 1, 2, 3]]
] 

for _ in range(N):
    t = list(map(int, input().split()))
    board.append(t)

a = []

for y in range(N):
    for x in range(M):
        if 0 < board[y][x] and board[y][x] < 6:
            a.append((y, x, board[y][x]))

ans = 987654321

def dfs(a, here, board):
    global N, M, ans, C 
    if here == len(a):
        cnt = 0 
        for y in range(N):
            for x in range(M):
                if board[y][x] == 0:
                    cnt += 1
        ans = min(ans, cnt)
        return
    y, x, val = a[here]
    for arrs in C[val]:
        new_board = copy.deepcopy(board)
        for direction in arrs:
            move(y, x, direction, new_board)
        dfs(a, here+1, new_board) 
dfs(a, 0, board)
print(ans)



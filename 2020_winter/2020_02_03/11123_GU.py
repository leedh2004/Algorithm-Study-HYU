import sys


def inRange(y, x):
    return ((0 <= y < H) and (0 <= x < W))


def sol(y, x):
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    q = [[y, x]]
    visited[y][x] = True

    while q:
        cur_y, cur_x = q.pop(0)
        for i in range(4):
            ny, nx = cur_y+dy[i], cur_x+dx[i]
            if inRange(ny, nx):
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if field[ny][nx] != '.':
                        q.append([ny, nx])


T = int(sys.stdin.readline())
for k in range(T):
    H, W = map(int, sys.stdin.readline().split())
    visited = [[False for _ in range(W)] for _ in range(H)]
    field = []

    for i in range(H):
        field.append(list(sys.stdin.readline().rstrip()))

    sheeps = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and field[i][j] == '#':
                sheeps += 1
                sol(i, j)
    print(sheeps)

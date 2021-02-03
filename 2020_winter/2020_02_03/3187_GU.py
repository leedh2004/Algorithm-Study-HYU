import sys


def inRange(y, x):
    return ((0 <= y < R) and (0 <= x < C))


def sol(y, x):
    global visited
    wolf = 0
    sheep = 0
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    q = [[y, x]]
    visited[y][x] = True
    if field[y][x] == 'v':
        wolf += 1
    elif field[y][x] == 'k':
        sheep += 1

    while q:
        cur_y, cur_x = q.pop(0)
        for i in range(4):
            ny, nx = cur_y+dy[i], cur_x+dx[i]
            if inRange(ny, nx):
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if field[ny][nx] == 'v':
                        wolf += 1
                    elif field[ny][nx] == 'k':
                        sheep += 1
                    if field[ny][nx] != '#':
                        q.append([ny, nx])

    if sheep > wolf:
        return [0, sheep]
    else:
        return [wolf, 0]


R, C = map(int, sys.stdin.readline().split())
field = []
visited = [[False for _ in range(C)] for _ in range(R)]
wolfs = 0
sheeps = 0

for i in range(R):
    field.append(list(sys.stdin.readline().rstrip()))

for i in range(R):
    for j in range(C):
        if not visited[i][j] and field[i][j] != '#':
            w, s = sol(i, j)
            wolfs += w
            sheeps += s
print(sheeps, wolfs)

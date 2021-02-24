import sys
# 파이썬 시간초과, pypy 성공
dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def inRange(y, x):
    return ((0 <= y < N) and (0 <= x < M))


def check(visited, y, x):
    if visited[y][x]:
        return False

    visited[y][x] = True
    q = [[y, x]]

    while q:
        cur_y, cur_x = q.pop(0)
        for i in range(4):
            ny, nx = cur_y+dy[i], cur_x+dx[i]
            if inRange(ny, nx) and not visited[ny][nx] and field[ny][nx] > 0:
                visited[ny][nx] = True
                q.append([ny, nx])

    return True


def time_goes():
    melt = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(1, N-1):
        for j in range(1, M-1):
            if field[i][j] > 0:
                minus = 0
                for k in range(4):
                    ny, nx = i+dy[k], j+dx[k]
                    if inRange(ny, nx) and field[ny][nx] == 0:
                        minus += 1
                if field[i][j] < minus:
                    melt[i][j] = -field[i][j]
                else:
                    melt[i][j] = -minus

    for i in range(1, N-1):
        for j in range(1, M-1):
            if field[i][j] > 0:
                field[i][j] += melt[i][j]

    visited = [[False for i in range(M)] for j in range(N)]
    flag = False
    for i in range(1, N-1):
        for j in range(1, M-1):
            if field[i][j] > 0:
                check(visited, i, j)
                flag = True
                break
        if flag:
            break
    # print(visited)
    for i in range(1, N-1):
        for j in range(1, M-1):
            if field[i][j] > 0 and not visited[i][j]:
                return True

    return False


def melted_all():
    for i in range(1, N-1):
        for j in range(1, M-1):
            if field[i][j] != 0:
                return False

    return True


N, M = map(int, sys.stdin.readline().split())
field = []
for i in range(N):
    field.append(list(map(int, sys.stdin.readline().split())))

time = 0
while True:
    time += 1
    if time_goes():
        print(time)
        break
    # print(field)
    if melted_all():
        print(0)
        break

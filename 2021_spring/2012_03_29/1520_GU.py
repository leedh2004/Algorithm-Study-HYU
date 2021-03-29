import sys
# 런타임 에러
sys.setrecursionlimit(10000)

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def inRange(y, x):
    return ((0 <= y < M) and (0 <= x < N))


def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1

    # 최초 방문
    if d[y][x] == -1:
        # 방문했다
        d[y][x] = 0
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if inRange(ny, nx) and field[y][x] > field[ny][nx]:
                d[y][x] += dfs(ny, nx)

    return d[y][x]


M, N = map(int, sys.stdin.readline().split())
field = []
for i in range(M):
    field.append(list(map(int, sys.stdin.readline().split())))
d = [[-1 for _ in range(N)] for _ in range(M)]
print(dfs(0, 0))

# print(d)

""" 시간 초과 (BFS) """
# while q:
#     y, x = q.popleft()
#     cur_h = field[y][x]
#     for i in range(4):
#         ny, nx = y+dy[i], x+dx[i]
#         if inRange(ny, nx) and cur_h > field[ny][nx]:
#             q.append([ny, nx])
#             d[ny][nx] += 1

# print(d[M-1][N-1])

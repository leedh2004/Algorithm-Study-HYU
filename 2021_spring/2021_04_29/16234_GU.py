import sys
from collections import deque


def inRange(y, x):
    return ((0 <= y < N) and (0 <= x < N))


def bfs(sy, sx):
    global visited
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    q = deque([[sy, sx]])
    visited[sy][sx] = True
    total_population = A[sy][sx]
    _union = [[sy, sx]]
    cnt = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if inRange(ny, nx) and not visited[ny][nx] and (L <= abs(A[y][x]-A[ny][nx]) <= R):
                total_population += A[ny][nx]
                visited[ny][nx] = True
                _union.append([ny, nx])
                cnt += 1
                q.append([ny, nx])
    if cnt > 1:
        after_move = total_population//cnt
        for uy, ux in _union:
            A[uy][ux] = after_move
        return False
    else:
        return True


N, L, R = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
T = 0

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    done = True
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if not bfs(i, j):
                    done = False
    if done:
        break
    else:
        T += 1

print(T)

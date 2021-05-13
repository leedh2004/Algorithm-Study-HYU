import sys
from collections import deque


def inRange(y, x):
    return (0 <= y < m) and (0 <= x < n)


def bfs(cnt, visited, sy, sx):
    visited[sy][sx] = True
    tmp[sy][sx] = cnt
    q = deque([[sy, sx]])
    # 서 북 동 남
    dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
    sz = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if not(sung[y][x] & (1 << i)):
                if inRange(ny, nx) and not visited[ny][nx]:
                    q.append([ny, nx])
                    tmp[ny][nx] = cnt
                    visited[ny][nx] = True
                    sz += 1

    return sz


n, m = map(int, sys.stdin.readline().split())
sung = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
tmp = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
cnt = 0
area = [0]
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            area.append(bfs(cnt, visited, i, j))

dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
two_sum = -1
for i in range(m):
    for j in range(n):
        for k in range(4):
            ny, nx = i+dy[k], j+dx[k]
            if inRange(ny, nx) and tmp[i][j] != tmp[ny][nx]:
                two_sum = max(two_sum, area[tmp[i][j]]+area[tmp[ny][nx]])
print(cnt)
print(max(area))
print(two_sum)

import sys
from collections import deque


def inRange(y, x):
    return (0 <= y < n) and (0 <= x < m)


def sol(visited, i, j):
    dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]
    cnt = 1
    q = deque([[i, j]])
    visited[i][j] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if inRange(ny, nx) and not visited[ny][nx] and pic[ny][nx]:
                visited[ny][nx] = True
                q.append([ny, nx])
                cnt += 1

    return cnt


n, m = map(int, sys.stdin.readline().split())
pic = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
_max = 0
for i in range(n):
    for j in range(m):
        if pic[i][j] and not visited[i][j]:
            cnt += 1
            _max = max(_max, sol(visited, i, j))
print(cnt)
print(_max)

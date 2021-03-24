import sys
from collections import deque

# 찾아보니 heap으로 푸는 방법도 있더라..


def inRange(y, x):
    return ((0 <= y < N) and (0 <= x < N))


INF = sys.maxsize
N = int(sys.stdin.readline())
rooms = []
for _ in range(N):
    rooms.append(list(map(int, list(sys.stdin.readline().rstrip()))))
q = deque([[0, 0]])
# visited = [[False for _ in range(N)] for _ in range(N)]
blacks = [[INF for _ in range(N)] for _ in range(N)]
# visited[0][0] = True
blacks[0][0] = 0
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

while q:
    y, x = q.popleft()
    cur_blacks = blacks[y][x]
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if inRange(ny, nx):
            if rooms[ny][nx] and blacks[ny][nx] > blacks[y][x]:
                blacks[ny][nx] = blacks[y][x]
                q.append([ny, nx])
            elif not rooms[ny][nx] and blacks[ny][nx] > blacks[y][x] + 1:
                blacks[ny][nx] = blacks[y][x] + 1
                q.append([ny, nx])
# print(blacks)

print(blacks[N-1][N-1])

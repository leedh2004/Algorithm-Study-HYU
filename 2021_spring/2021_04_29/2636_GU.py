import sys
from collections import deque

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]


def inRange(y, x):
    return ((0 <= y < N) and (0 <= x < M))


# check up down left right
def check_UDLR(y, x):
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if inRange(ny, nx):
            if grid[ny][nx] == 0:
                # hole 아닌 공기 맞닿음
                if not check_hole(ny, nx):
                    return False
        else:
            return False

    return True


# 지워질 테두리 2로 변환
def check_candidate(sy, sx, grid, visited):
    q = deque([[sy, sx]])
    visited[sy][sx] = True
    if not check_UDLR(sy, sx):
        grid[sy][sx] = 2

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if inRange(ny, nx) and grid[ny][nx] != 0 and not visited[ny][nx]:
                q.append([ny, nx])
                visited[ny][nx] = True

                if not check_UDLR(ny, nx):
                    grid[ny][nx] = 2


# hole인지 아닌지
def check_hole(sy, sx):
    visited2 = [[False for _ in range(M)] for _ in range(N)]
    q = deque([[sy, sx]])
    visited2[sy][sx] = True
    if sy == 0 or sy == N-1 or sx == 0 or sx == M-1:
        return False

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if inRange(ny, nx) and grid[ny][nx] == 0 and not visited2[ny][nx]:
                q.append([ny, nx])
                visited2[ny][nx] = True
                if ny == 0 or ny == N-1 or nx == 0 or nx == M-1:
                    return False

    return True


def melt():
    for i in range(1, N-1):
        for j in range(1, M-1):
            if grid[i][j] == 2:
                grid[i][j] = 0


N, M = map(int, sys.stdin.readline().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

# 구멍 일 것 같은거 하나에서 출발해서 visit 확인
# 벽 닿이면 공기
# 0 공기 1 안없어지는 것 2 없어질 것
time = 0
while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    cheese_cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if grid[i][j]:
                cheese_cnt += 1
                if not visited[i][j]:
                    check_candidate(i, j, grid, visited)

    done = True
    for i in range(1, N-1):
        for j in range(1, M-1):
            if grid[i][j] == 1:
                done = False
                break
        if not done:
            break

    if done:
        print(time+1)
        print(cheese_cnt)
        break
    else:
        melt()
        time += 1

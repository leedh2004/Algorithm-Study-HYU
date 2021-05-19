import sys
from collections import deque
sys.setrecursionlimit(10**9)
N, M = map(int, sys.stdin.readline().split())
board = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]

visited = [ [False for _ in range(M)] for _ in range(N) ]

#DFS 메모리 초괴.. 안좋은 문제임.
def dfs(y, x):
    global visited, N, M
    ret = 1
    for dy, dx in D:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1 and not visited[ny][nx]:
            visited[ny][nx] = True
            ret += dfs(ny, nx)
    return ret

A, B = 0, 0 # 개수, 넓이
q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            ret = dfs(i,j)
            A = A + 1
            B = max(ret,B)
            # q.append((i, j))
            # A += 1
            # ret = 0
            # while q:
            #     y, x = q.popleft()
            #     if visited[y][x]:
            #         continue
            #     visited[y][x] = True
            #     ret += 1
            #     for dy, dx in D:
            #         ny, nx = y + dy, x + dx
            #         if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1 and not visited[ny][nx]:
            #             q.append((ny, nx))
            # B = max(B, ret)

print(A)
print(B)
import sys
sys.setrecursionlimit(10**5)
n, Q = map(int, sys.stdin.readline().strip().split())
N = 2 ** n
board = [] 
for i in range(N):
    t = list(map(int, sys.stdin.readline().strip().split()))
    board.append(t)
L = list(map(int, sys.stdin.readline().strip().split()))
D = [(-1, 0), (1, 0), (0, 1), (0, -1)] 
for i in L:
    # 회전
    k = 2 ** i
    for y in range(0, N, k):
        for x in range(0, N, k):
            tmp = [ board[z][x:x+k] for z in range(y, y+k) ]
            for i in range(k):
                for j in range(k):
                    board[y + j][x + k - 1 - i] = tmp[i][j]
    # 얼음 감소   
    cnt = [ [0] * N for _ in range(N) ]
    for y in range(N):
        for x in range(N):
            if board[y][x] == 0:
                continue
            for j in range(4):
                ny, nx = y + D[j][0], x + D[j][1]
                if 0 <= ny < N and 0 <= nx < N:
                    if board[ny][nx] == 0:
                        cnt[y][x] += 1
                else:
                    cnt[y][x] += 1
    
    for y in range(N):
        for x in range(N):
            if cnt[y][x] >= 2:
                board[y][x] -= 1

print(sum([sum(i) for i in board]))

def dfs(y, x):
    board[y][x] = 0
    ret = 1
    for i in range(4):
        ny, nx = y + D[i][0], x + D[i][1]
        if 0 <= ny < N and 0 <= nx < N:
            if board[ny][nx] > 0:
                ret += dfs(ny, nx)
    return ret

max_cnt = 0
for y in range(N):
    for x in range(N):
        if board[y][x] > 0:
            max_cnt = max(max_cnt, dfs(y, x))

print(max_cnt)

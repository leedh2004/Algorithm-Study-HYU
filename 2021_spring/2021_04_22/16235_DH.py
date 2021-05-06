# //11:01
import sys 
import heapq
import copy
from collections import deque

N, M, K = map(int, sys.stdin.readline().strip().split())
A = [] 
for _ in range(N):
    t = list(map(int, sys.stdin.readline().strip().split()))
    A.append(t)

board = [ [5] * N for _ in range(N) ]
# board = copy.deepcopy(A)
trees = [ [deque() for _ in range(N) ] for _ in range(N) ]

for _ in range(M):
    y, x, z = map(int, sys.stdin.readline().strip().split())
    # heapq.heappush(trees, (z, y - 1, x - 1))
    trees[y-1][x-1].append(z)

D = [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]

for _ in range(K):
    # 봄 
    for i in range(N):
        for j in range(N):
            len_t = len(trees[i][j])
            for k in range(len_t):
                z = trees[i][j][k]
                if board[i][j] < z:
                    for _ in range(k, len_t):
                        board[i][j] += trees[i][j].pop() // 2
                    break
                else:
                    board[i][j] -= z
                    trees[i][j][k] += 1
    
    for i in range(N):
        for j in range(N):
            for z in trees[i][j]:
                if z % 5 == 0:
                    for l in range(len(D)):
                        ny, nx = i + D[l][0], j + D[l][1]
                        if 0 <= ny < N and 0 <= nx < N:
                            trees[ny][nx].appendleft(1)
            board[i][j] += A[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])
print(ans)




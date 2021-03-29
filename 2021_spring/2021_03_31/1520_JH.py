import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx,dy = [-1,1,0,0], [0,0,-1,1]
N,M = map(int,input().strip().split())  #문제에서 M이 코드의 N이고, 문제에서 N이 코드의 M이다.
mat = [ list(map(int,input().strip().split())) for _ in range(N)]
DP = [[-1 for _ in range(M)] for i in range(N)]
result = 0

def dfs(x,y):
    global result, DP

    if x == N-1 and y == M-1 :
        return 1

    if DP[x][y] != -1 :
        return DP[x][y]

    else :
        DP[x][y] = 0
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and mat[nx][ny] < mat[x][y] :
                flag = False
                DP[x][y] += dfs(nx,ny)

    return DP[x][y]

result = dfs(0,0)
print(result)

# 메모리 초과 뜸
# import sys
# input = sys.stdin.readline
# from collections import deque

# dx,dy = [-1,1,0,0], [0,0,-1,1]
# N,M = map(int,input().strip().split())  #문제에서 M이 코드의 N이고, 문제에서 N이 코드의 M이다.
# mat = [ list(map(int,input().strip().split())) for _ in range(N)]
# q = deque([[0,0]])
# result = 0

# while q :
#     for i in range(len(q)):
#         x,y = q.popleft()
#         for j in range(4):
#             nx,ny = x+dx[j], y+dy[j]
#             if 0<=nx<N and 0<=ny<M and mat[nx][ny] < mat[x][y] :
#                 if nx == N-1 and ny == M-1 :
#                     result += 1
#                 else :
#                     q.append([nx,ny])
# print(result)
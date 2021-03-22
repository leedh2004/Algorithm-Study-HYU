import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
mat = [list(map(int,input().strip())) for _ in range(n)]
dx,dy = [1,-1,0,0], [0,0,1,-1]
INF = 10e9
cost = [[INF for _ in range(n)] for i in range(n)]
cost[0][0] = 0
heap = [ [cost[0][0], 0,0] ]

while heap :
    c, x,y = heappop(heap)
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n :
            if mat[nx][ny] == 0:
                if cost[nx][ny] > cost[x][y] + 1:
                    cost[nx][ny] = cost[x][y] + 1
                    heappush(heap, [cost[nx][ny], nx, ny])
            else :
                if cost[nx][ny] > cost[x][y] :
                    cost[nx][ny] = cost[x][y]
                    heappush(heap, [cost[nx][ny], nx, ny])

print(cost[n-1][n-1])



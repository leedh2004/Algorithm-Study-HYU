from heapq import heappush, heappop
import sys

INF = sys.maxsize
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dij():
    d, q = [[INF]*M for _ in range(N)], []
    heappush(q, [maze[0][0], 0, 0])
    d[0][0] = 0
    while q:
        #w 작은 순으로 나오게 됨
        w, x, y = heappop(q)
        if x == N-1 and y == M-1:
            #도달 한 경우 1의 개수 -> 부셔야하는 개수
            print(d[N-1][M-1])
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                nw = w + maze[nx][ny]
                if nw < d[nx][ny]:
                    d[nx][ny] = nw
                    heappush(q, [nw, nx, ny])

M,N = map(int,input().split())
maze = [list(map(int,input().rstrip())) for _ in range(N)]
dij()

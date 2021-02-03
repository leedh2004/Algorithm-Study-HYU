import collections
import sys
sys.setrecursionlimit(10**6)
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
L = list()

def dfs(N,M,mat,visit,x,y):
    visit[x][y] = True
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<N and ny>=0 and ny<M and mat[nx][ny] == 1 and visit[nx][ny] == False:
            visit[nx][ny] = True
            dfs(N,M,mat,visit,nx,ny)

for i in range(T):   #main 함수
    M,N,K = map(int,input().split())
    mat = [[0]*M for _ in range(N)]
    visit = [[False]*M for _ in range(N)]
    result = 0
    for j in range(K):
        b,a= map(int,input().split())
        mat[a][b] = 1
    
    for o in range(N):
        for p in range(M):
            if mat[o][p] == 1 and visit[o][p] == False:
                dfs(N,M,mat,visit,o,p)
                result += 1
    print(result)
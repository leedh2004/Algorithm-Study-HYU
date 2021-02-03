# bfs로 구현

import queue
N,M = map(int,input().split())
mat = [list(map(int,input())) for _ in range(N)]
v_mat = [[10000]*M for _ in range(N)]
v_mat[0][0] = 1
visit = [[False]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start_x,start_y):
    q = queue.Queue()
    q.put((start_x,start_y))
    visit[start_x][start_y]=True

    while not q.empty():
        x,y = q.get()
        

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and mat[nx][ny] == 1 and visit[nx][ny] == False :
                
                q.put((nx,ny))
                visit[nx][ny] = True
                v_mat[nx][ny] = v_mat[x][y]+1

    print(v_mat[N-1][M-1])

bfs(0,0)








# dfs로 구현   예제 2번 안됨

# N,M = map(int,input().split())
# mat = [list(map(int,input())) for _ in range(N)]
# visit = [[False]*M for _ in range(N)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# result = 99999999999999999

# def dfs(start_x,start_y,count):      
#     global result
#     if start_x == N-1 and start_y == M-1 :
#         result = min(result,count)
#     visit[start_x][start_y] = True
#     for i in range(4):
#         nx = start_x+dx[i]
#         ny = start_y+dy[i]
#         if nx >= 0 and nx < N and ny >= 0 and ny < M and mat[nx][ny] == 1 and visit[nx][ny] == False :
#             dfs(nx,ny,count+1)

# dfs(0,0,1)
# print(result)
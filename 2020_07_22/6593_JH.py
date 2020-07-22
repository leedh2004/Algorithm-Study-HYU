#6593 - 상범빌딩

import collections

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

while True :
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0 :
        break

    mat = [ [] for _ in range(L) ]
    s_x, s_y, s_z = 0, 0, 0
    d_x, d_y, d_z = 0, 0, 0

    visit = [ [ [False for _ in range(C)] for i in range(R) ] for j in range(L) ]
    dis = [ [ [1000 for _ in range(C)] for i in range(R) ] for j in range(L) ]

    for i in range(L):
        for j in range(R):
            mat[i].append( list( input() ) )
            for k in range(C):
                if mat[i][j][k] == 'S':   #시작 지점 위치
                    s_x, s_y, s_z = j, k, i

                if mat[i][j][k] == 'E':  #출구 위치
                    d_x, d_y, d_z = j, k, i
                    
        enter = input()  #input으로 들어오는 enter 제거 하기 위해

    q = collections.deque()
    q.append([s_x,s_y,s_z])
    dis[s_z][s_x][s_y] = 0
    visit[s_z][s_x][s_y] = True

    while q : 
        x,y,z = q.popleft()

        for i in range(6):
            nx,ny,nz = x+dx[i], y+dy[i], z+dz[i]
            if nx>=0 and nx<R and ny>=0 and ny<C and nz>=0 and nz<L and visit[nz][nx][ny] == False and (mat[nz][nx][ny] == '.' or mat[nz][nx][ny] == 'E') :
                q.append([nx,ny,nz])
                visit[nz][nx][ny] = True
                dis[nz][nx][ny] = min(dis[nz][nx][ny], dis[z][x][y]+1)


    if visit[d_z][d_x][d_y] == False :
        print("Trapped!")
    else :
        print("Escaped in "+str(dis[d_z][d_x][d_y])+" minute(s).")



#1층만 bfs하고 다음층부터는 플로이드-와셜로 풀려고 했는데 시간초과가 분명해보임
# import collections
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]


# while True :
#     L, R, C = map(int, input().split())
#     if L == 0 and R == 0 and C == 0 :
#         break

#     mat = [ [] for _ in range(L) ]
#     s_x, s_y, s_z = 0, 0, 0
#     d_x, d_y, d_z = 0, 0, 0

#     dis = [ [ [1000 for _ in range(C)] for i in range(R) ] for j in range(L) ]

#     for i in range(L):
#         for j in range(R):
#             mat[i].append( list( input() ) )
#             for k in range(C):
#                 if mat[i][j][k] == 'S':   #시작 지점 위치
#                     s_x, s_y, s_z = j, k, i

#                 if mat[i][j][k] == 'E':  #출구 위치
#                     d_x, d_y, d_z = j, k, i
                    
#         enter = input()  #input으로 들어오는 enter 제거 하기 위해

#     q = collections.deque()
#     q.append([s_x,s_y])
#     visit = [ [False for _ in range(C)] for i in range(R) ]

#     while q :  #1층 거리 계산
#         x,y = q.popleft()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if nx>=0 and nx<R and ny>=0 and ny<C and mat[0][nx][ny] == '.' and visit[nx][ny] == False :
#                 q.append([nx,ny])
#                 visit[nx][ny] = True
#                 dis[0][nx][ny] = min(dis[nx][ny], dis[x][y]+1)

#     for _ in range(1,L,1):
#         for i in range(R):
#             for j in range(C):
#                 if mat[_][i][j] == '.' :
#                     mat[_][i][j] = mat[_-1][i][j]

#         for k in range(R):


    
    

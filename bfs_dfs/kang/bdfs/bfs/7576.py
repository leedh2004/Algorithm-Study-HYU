import collections          #queue를 deque로 바꾸면 시간초과 해결됨. 이것 때문에 시간 얼마나 쓴거냐;;
M,N = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
result = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = collections.deque()

def bfs(N,M,q) :
    global result
    count = 0

    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M and mat[nx][ny]== 0 :
                mat[nx][ny] = mat[x][y]+1
                q.append((nx,ny))
                count = mat[nx][ny]        #count는 트리의 높이+1임 왜냐하면 시작점일때 1로 가정 했기 때문에, mat[start_x][start_y]가 처음에 1이니까
    
    result = max(result,count-1)

def solve(N,M):
    global q
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1 :  #익은 토마토면 큐에 넣어줌, 시작점이 다양할 수 있으니까
                q.append((i,j))
    bfs(N,M,q)
                
    for a in mat:
        if not all(a) :
            return -1
    return result

print(solve(N,M))





# import queue          #시간초과 뜸
# M,N = map(int,input().split())
# mat = [list(map(int,input().split())) for _ in range(N)]
# result = 0
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# q = queue.Queue()

# def bfs(N,M,q) :
#     global result
#     count = 0

#     while not q.empty() :
#         x,y = q.get()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx>=0 and nx<N and ny>=0 and ny<M and mat[nx][ny]== 0 :
#                 mat[nx][ny] = mat[x][y]+1
#                 q.put((nx,ny))
#                 count = mat[nx][ny]        #count는 트리의 높이+1임 왜냐하면 시작점일때 1로 가정 했기 때문에, mat[start_x][start_y]가 처음에 1이니까
    
#     result = max(result,count-1)

# def solve(N,M):
#     global q
#     for i in range(N):
#         for j in range(M):
#             if mat[i][j] == 1 :  #익은 토마토면 큐에 넣어줌, 시작점이 다양할 수 있으니까
#                 q.put((i,j))
#     bfs(N,M,q)
                
#     for i in range(N):
#         for j in range(M):
#             if mat[i][j] == 0:  #모두 익힌 후 안익은 토마토가 있으면
#                 return -1
#     return result

# print(solve(N,M))







#예제 2번을 해결하지 못함, 즉 토마토가 두 저짐이상에서부터 익는 것을 계산하지 못함
# import queue
# M,N = map(int,input().split())
# mat = [list(map(int,input().split())) for _ in range(N)]
# result = 0
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# def bfs(start_x,start_y,N,M) :
#     global result
#     q = queue.Queue()
#     q.put((start_x,start_y))
#     count = 0

#     while not q.empty() :
#         x,y = q.get()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx>=0 and nx<N and ny>=0 and ny<M and mat[nx][ny]== 0 :
#                 mat[nx][ny] = mat[x][y]+1
#                 q.put((nx,ny))
#                 count = mat[nx][ny]
    
#     result = max(result,count-1)

# def solve(N,M):
#     for i in range(N):
#         for j in range(M):
#             if mat[i][j] > 0 :  #익은 토마토면
#                 bfs(i,j,N,M)
#                 print(mat)
#     for i in range(N):
#         for j in range(M):
#             if mat[i][j] == 0:  #모두 익힌 후 안익은 토마토가 있으면
#                 return -1
#     return result

# print(solve(N,M))
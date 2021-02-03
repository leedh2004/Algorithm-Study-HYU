import heapq

M,N = map(int,input().split())
mat = [ list(input()) for i in range(N) ]
visit = [ [False for _ in range(M)] for _ in range(N) ]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

heap = []
heapq.heappush(heap,[0,0,0])
visit[0][0] = True

while heap :
    c,x,y = heapq.heappop(heap)
    if x == N-1 and y == M-1 :
        print(c)
        break

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if(nx>=0 and nx<N and ny>=0 and ny<M and visit[nx][ny] == False):
            if mat[nx][ny] == '1':
                heapq.heappush(heap, [c+1,nx,ny])
            else :
                heapq.heappush(heap, [c,nx,ny])
            visit[nx][ny] = True
            







# import collections      메모리 초과 나옴

# M,N = map(int,input().split())
# mat = [ list(input()) for i in range(N) ]
# visit = [ [False for _ in range(M)] for _ in range(N) ]
# result = [ [ [1e9,1e9] for _ in range(M) ] for _ in range(N) ] # [부셔야하는 벽의 수, 거리]

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# q = collections.deque()
# q.append([0,0])
# visit[0][0] = True
# result[0][0][1] = 0
# result[0][0][0] = 0

# while q :
#     x,y = q.popleft()
#     for i in range(4):
#         nx,ny = x+dx[i], y+dy[i]
#         if(nx>=0 and nx<N and ny>=0 and ny<M and result[nx][ny][1]>result[x][y][1]):
#             if mat[nx][ny] == '1':
#                 result[nx][ny][0] = min(result[nx][ny][0],result[x][y][0]+1)
#             else :
#                 result[nx][ny][0] = min(result[nx][ny][0],result[x][y][0])
#             result[nx][ny][1] = result[x][y][1]+1
#             q.append([nx,ny])


# print(result[N-1][M-1][0])
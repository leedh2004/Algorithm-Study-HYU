#정답 오름차순으로 정렬해줘야함, 안해줘서 틀림 ㅠ, sorted는 정렬된 값 변환 list.sort()는 리스트 내부에서 정렬시킴

import queue
N = int(input())
mat = [list(map(int,input())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = list()
visit = [[False]*N for _ in range(N)]

def bfs(start_x,start_y,N):
    q = queue.Queue()
    q.put((start_x,start_y))
    count = 1
    while not q.empty():
        x,y = q.get()
        visit[x][y] = True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<N and mat[nx][ny] == 1 and visit[nx][ny] == False:
                q.put((nx,ny))
                visit[nx][ny] = True
                count+=1
    result.append(count)

def solve(N):
    count = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == False and mat[i][j] == 1:
                count +=1
                bfs(i,j,N)
    print(count)

solve(N)
for i in sorted(result):
    print(i)
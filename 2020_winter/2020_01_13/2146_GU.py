import sys

def in_range(y,x):
    return ((0<=y) and (y<N) and (0<=x) and (x<N))

def count_sum(nara,N):
    visited= [[False]*N for _ in range(N)]
    cnt = 1
    
    for i in range(N):
        for j in range(N):
            if nara[i][j] > 0 and not visited[i][j]:
                nara[i][j] = cnt
                bfs(visited,[[i,j]],cnt)
                cnt += 1

def bfs(visited,q,num):
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]

    while q:
        y,x = q.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if in_range(ny,nx) and not visited[ny][nx] and nara[ny][nx] > 0:
                visited[ny][nx] = True
                nara[ny][nx] = num
                q.append([ny,nx])

def expand_bfs(q,num):
    dist = [[0]*N for _ in range(N)]
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]

    # 먼저 동서남북 돌고 다리 지을 수 있는지 확인
    y,x = q.pop(0)
    dist[y][x] = -1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(ny,nx) and dist[ny][nx] == 0 and nara[ny][nx] == 0:
            dist[ny][nx] = 1
            q.append([ny,nx])

    # 섬 안에서 동서남북 돈 경우(다리 못지음)
    if not q: return -1

    while q:
        # 이거 pop() 으로 했다가 진짜 시간 많이 걸려서 삽질했다
        y,x = q.pop(0)
        #print(dist)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not in_range(ny,nx) or dist[ny][nx] > 0: continue
            if nara[ny][nx] != 0 and nara[ny][nx]!= num:
                #print("expand",nara[ny][nx])
                return dist[y][x]
            elif dist[ny][nx] == 0 and nara[ny][nx] == 0:
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny,nx])
    return -1


#섬이란 동서남북으로 육지가 붙어있는 덩어리
N = int(sys.stdin.readline())
nara = []
for i in range(N):
    nara.append(list(map(int,sys.stdin.readline().split())))

count_sum(nara,N)

bridge = 99999
for i in range(N):
    for j in range(N):
        if nara[i][j] > 0: 
            res = expand_bfs([[i,j]],nara[i][j])
            if res > 0: 
                bridge = min(bridge,res)
                
print(bridge)
                


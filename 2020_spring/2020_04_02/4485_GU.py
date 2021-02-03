import sys

INF = sys.maxsize

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dijkstra(map_,N,cnt):
    dist = [[INF]*N for _ in range(N)]
    dist[0][0] = 0
    q= [[map_[0][0],0,0]]
    while(q):
        [w,y,x] = q.pop(0)
        if y== N-1 and x == N-1:
            print("Problem %d: %d"%(cnt,w))
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(0<= ny < N and 0<= nx < N):
                nw = w + map_[ny][nx]
                if(nw < dist[ny][nx]):
                    dist[ny][nx] = nw
                    q.append([nw,ny,nx])
        q.sort()
            
            
cnt =1                
while(True):
    N = int(sys.stdin.readline())
    if N==0:
        break
    map_ = [[0]*N for _ in range(N)]
    for i in range(N):
        line = list(map(int,sys.stdin.readline().split()))
        map_[i]=line
    dijkstra(map_,N,cnt)
    cnt +=1
    
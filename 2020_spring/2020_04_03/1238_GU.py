import sys
from heapq import heappush, heappop
INF = sys.maxsize

def dij(start):
    dist = [INF] *(N+1)
    q =[]
    heappush(q,[0,start])
    dist[start]= 0
    while q:
        time,cur = heappop(q)
        """newList = [x for x in path if x[0]==cur]
        for i in range(len(newList)):
            s,e,t = newList[i]
            nt = t + time
            if(dist[e]> nt):
                dist[e] = nt
                heappush(q,[nt,e])"""
        for i in range(len(path[cur])):
            e = path[cur][i][0]
            t = path[cur][i][1]
            nt = t + time
            if(dist[e]> nt):
                dist[e] = nt
                heappush(q,[nt,e])
    return dist


N,M,X = map(int,sys.stdin.readline().split())

#path = [[0]*3 for _ in range(M)]
path = [[]*(N+1) for _ in range(N+1)]
for i in range(M):
    #path[i] = list(map(int,sys.stdin.readline().split()))
    s,e,t = map(int,sys.stdin.readline().split())
    path[s].append([e,t])

d = dij(X)

for i in range(1,N+1):
    if i == X:
        continue
    nd = dij(i)
    d[i] += nd[X]
d[0] = 0
print(max(d))


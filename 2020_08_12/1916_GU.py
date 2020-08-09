import sys
from heapq import heappush,heappop

INF = sys.maxsize
input = sys.stdin.readline

def dij():
    d,q = [INF] * (N+1) , []
    heappush(q,[0,start])
    d[start] = 0
    while q:
        w,u = heappop(q)
        for i in range(len(dist[u])):
            weight, v = dist[u][i]
            if d[v] > d[u] + weight:
                d[v] = d[u] + weight
                heappush(q,[d[v],v])
    print(d[dest])

N = int(input())
M = int(input())
dist = [[] for _ in range(N+1)]
for i in range(M):
    u,v,w = map(int,input().split())
    dist[u].append([w,v])
start,dest = map(int,input().split())
dij()
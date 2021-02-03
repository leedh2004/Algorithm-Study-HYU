import sys
from heapq import heappush,heappop

INF = sys.maxsize
input = sys.stdin.readline

def dij():
    d,q = [INF] * (V+1) , []
    heappush(q,[0,S])
    d[S] = 0
    while q:
        _ ,start = heappop(q)
        link = dist[start]
        for i in range(len(link)):
            weight, v = link[i]
            if d[v] > d[start] + weight:
               d[v] = d[start] + weight
               heappush(q,[d[v],v])
    for i in range(1,V+1):
        if d[i] != INF: print(d[i])
        else: print("INF")

V,E = map(int,input().split())
S = int(input())
dist = [[] for _ in range(V+1)]
for i in range(E):
    u,v,w = map(int,input().split())
    dist[u].append([w,v])
dij()
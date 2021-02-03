import sys

INF = sys.maxsize
input = sys.stdin.readline

N,M = map(int,input().split())
d = [INF] * (N+1)
d[1] = 0
ways = [[] for _ in range(N+1)]
for i in range(M):
    a,b,c = map(int,input().split())
    ways[a].append([b,c])
cycle = False
for i in range(1,N+1):
    for start in range(1,N+1): # 출발지
        for k in range(len(ways[start])):
            dest = ways[start][k][0]
            time = ways[start][k][1]
            if d[dest] > d[start] + time and d[start] != INF:
                d[dest] = d[start] + time
                if i == N: cycle = True
if cycle: print(-1)
else:
    if N == 1:
        print(d[1])
    else:
        for i in range(2,N+1):
            if d[i] != INF: print(d[i])
            #INF -> 경로 없음
            else: print(-1)
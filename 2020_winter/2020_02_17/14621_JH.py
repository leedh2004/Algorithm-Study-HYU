import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N,M = map(int, input().split())
university = list(input().split())
INF = 10e20
edge = []

uni = [i for i in range(N)]

for i in range(M):
    u,v,d = map(int,input().split())
    u, v = u-1, v-1
    if university[u] != university[v] :
        edge.append([d,u,v])

def find(x):
    global uni
    if uni[x] == x :
        return x
    else :
        y = find(uni[x])
        uni[x] = y
        return y


def union(x,y):
    global uni
    tmp_x, tmp_y = find(x), find(y)
    if tmp_x != tmp_y :
        uni[tmp_y] = tmp_x

def kruskal():
    global N, uni, edge
    edge.sort()
    cost = 0
    visit = [False for _ in range(N)]

    for c,s,d in edge :
        if s!=d and find(s) != find(d):
            cost += c
            union(s,d)
            visit[s], visit[d] = True, True

    for i in visit :
        if i == False:
            print(-1)
            return
    print(cost)
        
kruskal()


# import sys
# input = sys.stdin.readline
# from heapq import heappush, heappop

# N,M = map(int, input().split())
# university = list(input().split())
# adj = { i:[] for i in range(N)  }
# INF = 10e20
# result = 10e20

# for i in range(M):
#     u,v,d = map(int,input().split())
#     u,v = u-1,v-1
#     if university[u] == university[v] :
#         continue
#     adj[u].append([d,v])
#     adj[v].append([d,u])

# def dij(start):
#     global N, INF, adj
#     heap = []
#     dis = [INF for _ in range(N)]
#     result = 0

#     heappush(heap, [0,start])
#     dis[start] = 0

#     while heap :
#         now_c, now_v = heappop(heap)
#         for c,d in adj[now_v]:
#             if dis[d] > now_c + c :
#                 dis[d] = now_c + c 
#                 heappush(heap, [dis[d],d])

#     for i in dis :
#         if i == INF :
#             return INF
#         result += i

#     return result


# for i in range(N):
#     ret = dij(i)
#     if ret == INF :
#         continue
#     result = min(result, ret)


# if result == INF :
#     print(-1)
# else :
#     print(result)

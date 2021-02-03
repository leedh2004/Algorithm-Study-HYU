import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
mat = [[] for _ in range(N)]
for i in range(M):
    s,d,c = map(int,input().split())
    mat[s-1].append([c,d-1])
    mat[d-1].append([c,s-1])
INF = 10e9
dis = [INF for i in range(N)]
dis[1] = 0

def dij(start):
    global INF, N, dis, mat
    heap = []
    heappush(heap, [0,start])

    while heap :
        tmp_cost, tmp_v = heappop(heap)
        for c,v in mat[tmp_v]:
            now_c = tmp_cost+c
            if now_c < dis[v] :
                dis[v] = now_c
                heappush(heap,[now_c, v])

DP = [0 for _ in range(N)]
DP[1] = 1

def solution(now_point):
    global dis, mat, DP
    if DP[now_point] != 0 :
        return DP[now_point]

    for c,v in mat[now_point] :
        if dis[now_point] > dis[v]:
            DP[now_point] += solution(v)
    
    return DP[now_point]

dij(1)
print(solution(0))

#메모리초과

# import sys
# from heapq import heappush, heappop
# from collections import deque
# input = sys.stdin.readline

# N,M = map(int, input().split())
# mat = [[] for _ in range(N)]
# for i in range(M):
#     s,d,c = map(int,input().split())
#     mat[s-1].append([c,d-1])
#     mat[d-1].append([c,s-1])
# INF = 10e9
# dis = [INF for i in range(N)]
# dis[1] = 0

# def dij(start):
#     global INF, N, dis, mat
#     heap = []
#     heappush(heap, [0,start])

#     while heap :
#         tmp_cost, tmp_v = heappop(heap)
#         for c,v in mat[tmp_v]:
#             now_c = tmp_cost+c
#             if now_c < dis[v] :
#                 dis[v] = now_c
#                 heappush(heap,[now_c, v])

# def solution():
#     global dis, mat

#     dij(1)
#     # print(dis)

#     q = deque()
#     q.append(0)

#     result = 0
#     dis[1] = -1

#     while q :
#         for i in range(len(q)):
#             now_v = q.popleft()
#             now_dis = dis[now_v]
#             for j in mat[now_v]:
#                 if now_dis > dis[j[1]] :
#                     if j[1] == 1 :
#                         result += 1
#                     else :
#                         q.append(j[1])

#     print(result)

# solution()
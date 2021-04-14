# 다익스트라 10번 (야쿠르트 아줌마 9번, 나 1번) >> 왜 시간초과 ??
import sys
input = sys.stdin.readline
from collections import defaultdict
from heapq import heapify, heappop, heappush
from copy import deepcopy

V,E = map(int, input().strip().split())
INF = 10e9
dis = [[INF for _ in range(V)] for i in range(V)]

for i in range(E):
    s,e,c = map(int,input().strip().split())
    s,e = s-1, e-1
    dis[s][e], dis[e][s] = min(dis[s][e],c), min(dis[e][s],c)

Y_L = list(map(lambda x : int(x)-1,input().strip().split()))
Y_T = defaultdict(list)

start = int(input().strip())-1

now_node, now_time = Y_L[0], 0
Y_T[now_node].append(now_time)


def dijk(s,e=None, start_time=0):
    global V, INF
    tmp_dis = [INF for _ in range(V)]
    tmp_dis[s] = start_time
    heap = [[start_time,s]]
    heapify(heap)

    while heap :
        c,t = heappop(heap)
        for i in range(V):
            tmp_cost = dis[t][i] + c
            # print(tmp_cost, tmp_dis[i], i)
            if tmp_dis[i] > tmp_cost :
                tmp_dis[i] = tmp_cost
                heappush(heap, [tmp_cost, i])

    # print("tmp_dis : ",tmp_dis)

    if e != None :
        if tmp_dis[e] == INF :
            return -1
        else :
            return tmp_dis[e]

    else :
        return tmp_dis

result = INF

now_node = Y_L[0]
now_time = 0
for i in range(1, len(Y_L)):
    next_node = Y_L[i]
    tmp_time = dijk(now_node,next_node, now_time)
    if tmp_time == -1 :
        continue
    now_time = tmp_time
    Y_T[next_node].append(now_time)
    now_node = next_node


print(Y_T)

dis = dijk(start)
# print(dis)

for (node, times) in Y_T.items() :
    for time in times :
        if dis[node] <= time :
            result = min(result, node)
            break

if result == INF :
    print(-1)
else :
    print(result+1)


# 플로이드 와샬로 풀었는데 시간 초과
# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# V,E = map(int, input().strip().split())
# INF = 10e9
# dis = [[INF for _ in range(V)] for i in range(V)]

# for i in range(E):
#     s,e,c = map(int,input().strip().split())
#     s,e = s-1, e-1
#     dis[s][e], dis[e][s] = min(dis[s][e],c), min(dis[e][s],c)

# Y_L = list(map(lambda x : int(x)-1,input().strip().split()))
# Y_T = defaultdict(list)

# start = int(input().strip())-1

# for k in range(V):
#     for i in range(V):
#         for j in range(V):
#             if dis[i][j] > dis[i][k] + dis[k][j] :
#                 dis[i][j] = dis[i][k] + dis[k][j]

# now_node, now_time = Y_L[0], 0
# Y_T[now_node].append(now_time)

# for i in range(1, len(Y_L)) :
#     next_node = Y_L[i]
#     if dis[now_node][next_node] == INF :
#         continue
#     now_time = dis[now_node][next_node]+now_time
#     Y_T[next_node].append(now_time)
#     now_node = next_node

# # print(dis)
# # print(Y_L)
# # print(Y_T)

# result = INF

# for (node, times) in Y_T.items() :
#     for time in times :
#         if dis[start][node] <= time :
#             result = min(result, node)

# if result == INF :
#     print(-1)
# else :
#     print(result+1)
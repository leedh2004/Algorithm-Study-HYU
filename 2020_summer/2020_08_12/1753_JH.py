# from heapq import heappush, heappop

# V, E = map(int, input().split())
# K = int(input())
# adj = [[50000*50000 for _ in range(V)] for _ in range(V)]
# dis = [50000*50000 for _ in range(V)]
# dis[K-1] = 0
# heap = []
# heappush(heap,K-1)

# for i in range(E):
#     u,v,w = map(int,input().split())
#     adj[u-1][v-1] = w

# while heap : 
#     t = heappop(heap)
#     for i in range(V):
#         if dis[i] > dis[t] + adj[t][i] :
#             dis[i] = dis[t] + adj[t][i]
#             heappush(heap,i)

# for i in dis :
#     if(i == 50000*50000):
#         print("INF")
#     else :
#         print(i)

from heapq import heappush, heappop

V, E = map(int, input().split())
K = int(input())
adj = [[] for _ in range(V)]
dis = [30000000 for _ in range(V)]
dis[K-1] = 0
heap = []
heappush(heap,[0,K-1])

for i in range(E):
    u,v,w = map(int,input().split())
    adj[u-1].append([v-1,w])

while heap :
    tmp_dis,t = heappop(heap)
    for node,wei in adj[t] :
        if dis[node] > tmp_dis + wei :
            dis[node] = tmp_dis + wei
            heappush(heap,[dis[node],node])

for i in dis :
    if(i == 30000000):
        print("INF")
    else :
        print(i)
from heapq import heappush, heappop

N = int(input())
M = int(input())
adj = [[] for _ in range(N)]
dis = [1e9 for _ in range(N)]
heap = []
for i in range(M) :
    u,v,w = map(int,input().split())
    adj[u-1].append([v-1,w])

s,d = map(int,input().split())
dis[s-1] = 0
heappush(heap,[0,s-1])

while heap :
    tmp_dis, t = heappop(heap)
    for node, wei in adj[t] :
        if dis[node] > tmp_dis + wei :
            dis[node] = tmp_dis + wei
            heappush(heap,[dis[node],node])

print(dis[d-1])
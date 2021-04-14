import sys
import heapq

def dijikstra(s):
    global d, V
    dist = [ INF ] * (V+1)
    pq = []
    heapq.heappush(pq, (0, s))
    while pq:
        distance, here = heapq.heappop(pq)
        distance = -distance
        if distance >= dist[here]:
            continue
        dist[here] = distance
        for (nxt_distance, nxt) in d[here]:
            nxt_distance += distance
            if nxt_distance < dist[nxt]:
                heapq.heappush(pq,((-nxt_distance, nxt)))
    return dist

V, E = map(int, sys.stdin.readline().rstrip().split()) 
INF = 10987654321

d = [ [] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    d[u].append((w, v)) 
    d[v].append((w, u))

S = list(map(int, sys.stdin.readline().rstrip().split()))
# dist[i]는 요구르트 아줌마가 i번째 Vertex에 도달하는 시간
dist = [ INF ] * (V+1)
# l 요구르트 아줌마의 현재 위치
l = S[0]
cur = 0
dist[l] = 0

for idx, v in enumerate(S):
    if idx == 0: continue
    D = dijikstra(l)
    if D[v] < INF:
        cur += D[v] 
        dist[v] = cur
        l = v
# dist2[i]는 내가 각 노드에 도달하는 시간
s = int(sys.stdin.readline().rstrip())
dist2 = dijikstra(s)
ret = -1
for i in range(len(dist)):
    if dist[i] == INF or dist2[i] == INF:
        continue
    if dist[i] > dist2[i]:
        ret = i
        break
print(ret)
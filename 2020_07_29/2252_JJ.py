import sys
import heapq

n,m = map(int,sys.stdin.readline().split())
#인접행렬 -> 메모리초과라서 인접리스트로 변경
adj = [[ ] for _ in range(n+1)]

#차수
degree = [0 for _ in range(n+1)]

#연결관계
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    adj[a].append(b)
    degree[b] = degree[b] + 1

pq = []

for i in range(1,n+1):
    if degree[i]==0:
        degree[i] = -1
        heapq.heappush(pq,i)

while pq:
    now = heapq.heappop(pq)
    print(now,end=" ")
    for i in adj[now]:
        degree[i] = degree[i] - 1
        if degree[i]==0:
            degree[i] = -1
            heapq.heappush(pq,i)

print("")

    


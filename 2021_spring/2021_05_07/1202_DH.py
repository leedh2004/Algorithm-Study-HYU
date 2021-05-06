import sys 
import heapq

N, K = map(int, sys.stdin.readline().strip().split())

j = []
C = []
pq = []

for _ in range(N):
    m, v = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(j, (m, v))

for _ in range(K):
    c = int(sys.stdin.readline().strip())
    C.append(c)

C = sorted(C)
ans = 0 
for c in C:
    while j and c >= j[0][0]:
        m, v = heapq.heappop(j)
        heapq.heappush(pq, (-v))
    if pq:
        ans += -(heapq.heappop(pq))
print(ans) 
import sys
from heapq import heappop, heappush

# 보석 N개 가방 K개
N, K = map(int, sys.stdin.readline().split())
jewelry = []
C = []
ans = 0
# 무게, 가격
for _ in range(N):
    heappush(jewelry, list(map(int, sys.stdin.readline().split())))
# 무게
for _ in range(K):
    C.append(int(sys.stdin.readline()))
C.sort()
candidate = []
for i in range(K):
    while jewelry and C[i] >= jewelry[0][0]:
        heappush(candidate, -heappop(jewelry)[1])
    # C[i] 보다 용량 작은 것들이 가격 큰 순으로 정렬되어 있다.
    if candidate:
        ans += -(heappop(candidate))
print(ans)

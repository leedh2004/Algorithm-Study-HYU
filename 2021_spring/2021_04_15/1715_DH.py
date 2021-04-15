# 삼성기출아님
import heapq
N = int(input())
h = []
for _ in range(N):
    v = int(input())
    heapq.heappush(h, v)

ret = 0

while h:
    a = heapq.heappop(h)
    if not h:
        break
    b = heapq.heappop(h)
    ret += (a + b)
    heapq.heappush(h, (a+b))

print(ret)
    
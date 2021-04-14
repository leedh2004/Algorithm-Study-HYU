import heapq
import sys

input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
  tmp = int(input())
  heapq.heappush(h,tmp)

ans = 0

while len(h)>1:
  a,b = heapq.heappop(h),heapq.heappop(h)
  abSum = a + b
  ans = ans + abSum
  heapq.heappush(h,abSum)

print(ans)



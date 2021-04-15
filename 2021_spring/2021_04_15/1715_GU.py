from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline())
cards = []
for _ in range(N):
    heappush(cards, int(sys.stdin.readline()))
cnt = 0
while len(cards) > 1:
    A = heappop(cards)
    B = heappop(cards)
    cnt += (A+B)
    heappush(cards, A+B)
print(cnt)

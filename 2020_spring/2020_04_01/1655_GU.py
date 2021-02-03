import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(1,N+1):
    heapq.heappush(heap, int(sys.stdin.readline()))
    if i%2 ==0:
        idx = i//2-1
    else:
        idx == i//2
    


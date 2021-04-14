import sys
input = sys.stdin.readline
from heapq import heapify, heappush, heappop

N = int(input().strip())
L = []
for i in range(N):
    L.append(int(input().strip()))

heapify(L)
result = 0
heap_len = len(L)

if heap_len == 1 :
    print(result)

else :
    while heap_len != 1 :
        tmp = heappop(L)+ heappop(L)
        
        if heap_len == 2 :
            heappush(L, tmp)
            break
        else :
            result += tmp
            heappush(L, tmp)
            heap_len -= 1

    result += heappop(L)

    print(result)
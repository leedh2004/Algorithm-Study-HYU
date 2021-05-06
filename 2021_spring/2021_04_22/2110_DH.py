import heapq
from bisect import bisect_left, bisect_right
N, C = map(int, input().split())

lis = []

for _ in range(N):
    x = int(input())
    lis.append(x)

lis = sorted(lis)


G = [lis[0], lis[-1]]
H = []
heapq.heappush(H, (lis[0]-lis[len(lis)-1], 0, len(lis)-1))

ans = 10987654321
for _ in range(C-2):
    dist, i, j = heapq.heappop(H)
    ans = min(ans, -dist)
    mid = (lis[i] + lis[j]) // 2
    midIdx = bisect_left(lis, mid)
    # 새로운 공유기의 Idx를 구함.
    # 0인 경우로 분기처리 해야함.
    Idx = -1
    if midIdx == 0:
        Idx = midIdx
    else:
        # print(midIdx)
        midIdx2 = midIdx - 1
        C1 = lis[midIdx]
        C2 = lis[midIdx2]
        # print(mid, C1, C2, lis[i], lis[j])
        # print(C1 - lis[i], lis[j] - C1, C2 - lis[i], lis[j] - C2)
        C1 = min(C1 - lis[i], lis[j] - C1) # 4 - 1, 6 - 4 
        C2 = min(C2 - lis[i], lis[j] - C2) # 0,5
        # print("?", C1, C2)
        Idx = midIdx if C1 > C2 else midIdx2 
    # G.append(lis[Idx])
    heapq.heappush(H, (lis[i] - lis[Idx], i, Idx))
    heapq.heappush(H, (lis[Idx] - lis[j], Idx, j))


# G = sorted(G)
# print(G)
while H:
    dist, i, j = heapq.heappop(H)
    dist = -dist
    # print(dist, i, j)
    ans = min(ans, dist)
print(ans) 
    
    

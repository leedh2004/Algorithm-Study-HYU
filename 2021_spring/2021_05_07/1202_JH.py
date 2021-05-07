import sys
input = sys.stdin.readline
from heapq import heapify, heappop, heappush

N, K = map(int,input().strip().split())
heap = []
for _ in range(N):
    M, V = map(int, input().strip().split())
    heappush(heap, [M,V])

bags = []
for _ in range(K):
    heappush(bags, int(input()))

able = []
result = 0

while bags :
    now_c = heappop(bags)

    while heap and heap[0][0] <= now_c :
        tmp_m, tmp_v = heappop(heap)
        heappush(able, -tmp_v)

    if able :
        result -= heappop(able)

print(result)




#시간초과 ;;
# N, K = map(int,input().strip().split())
# heap = []
# for _ in range(N):
#     M, V = map(int, input().strip().split())
#     if V == 0 :
#         continue
#     heap.append([-V,M])
# heapify(heap)
# bags = [ [int(input().strip()), False] for _ in range(K) ]
# bags.sort()

# count = 0
# result = 0

# while count < K and heap :
#     v, m = heappop(heap)

#     for i in range(K):
#         if bags[i][1] :
#             continue
#         if bags[i][0] >= m :
#             bags[i][1] = True
#             count += 1
#             result -= v
#             break

# print(result)
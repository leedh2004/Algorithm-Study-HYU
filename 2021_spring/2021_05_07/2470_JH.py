# 파이썬 시간복잡도
# https://wiki.python.org/moin/TimeComplexity
# 파이썬 list sort의 amortized worst case에 대한 시간 복잡도도 nlogn 이라고 합니다... 그래서 아래 코드보다 빠른듯

# 그냥 sort 하는게 더 빠름
# from heapq import heapify, heappop
# import time

# start = time.time()
# L1 = [i for i in range(1000,-1,-1)]
# L1.sort()
# print(time.time()-start)

# start = time.time()
# L2 = [i for i in range(1000,-1,-1)]
# L3 = []
# heapify(L2)
# while L2 :
#     L3.append(heappop(L2))
# print(time.time()-start)


import sys
input = sys.stdin.readline

N = int(input().strip())
L = list(map(int,input().strip().split()))
L.sort()
left_idx, right_idx = 0, N-1
left, right = 0,N-1
gap = L[left_idx] + L[right_idx]

if gap == 0 :
    print(L[left_idx], L[right_idx])

else :
    while left < right :
        tmp_gap = L[left]+L[right]
        
        if abs(tmp_gap) < abs(gap) :
            gap = tmp_gap
            left_idx, right_idx = left, right

            if gap == 0 :
                break
        
        if tmp_gap < 0 :
            left += 1
        else :
            right -= 1

    print(L[left_idx], L[right_idx])

        



# 시간초과
# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# L = list(map(int, input().strip().split()))
# gap = L[0] + L[1]
# left_idx, right_idx = 0,1

# for i in range(N):
#     for j in range(i+1,N):
#         tmp_gap = L[i] + L[j]
#         if abs(gap) > abs(tmp_gap) :
#             gap = tmp_gap
#             left_idx, right_idx = i,j

# print(L[left_idx], L[right_idx])
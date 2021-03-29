import sys

N, C = map(int, sys.stdin.readline().split())
d = [[0 for _ in range(C+1)] for _ in range(N+1)]
d[2][0] = 1
d[2][1] = 1

for i in range(3, N+1):
    for j in range(C+1):
        if d[i-1][j] != 0:
            for k in range(i):
                if j+k < C+1:
                    d[i][j+k] = (d[i][j+k] + d[i-1][j]) % 1000000007
                else:
                    break
        else:
            break

print(d[N][C])

# (1,2) = 0 / (2,1) = 1

# nums = [x for x in range(1, N+1)]
# prefix_sum = [0 for _ in range(1, N+1)]
# prefix_sum[0] = 1
# for i in range(1, N):
#     prefix_sum[i] = prefix_sum[i-1] + nums[i]
# # print(prefix_sum)
# # 메모리 초과가 떴어요 !
# P = list(permutations(nums, N))
# chaos = 0

# for i in range(len(P)):
#     arr = P[i]
#     cnt = 0
#     flag = False
#     if arr[0] != prefix_sum[0]:
#         cnt += 1
#     cur = arr[0]
#     for j in range(1, N):
#         cur += arr[j]
#         if cur != prefix_sum[j]:
#             cnt += 1
#         if cnt > C:
#             break
#     if cnt == C:
#         chaos = (chaos+1) % 1000000007
# print(chaos)

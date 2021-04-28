import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int,input().strip().split()))
INF = -10e10
DP = [INF for _ in range(N)]
DP[0] = L[0]

for i in range(1,N,1):
    DP[i] = max(DP[i-1]+L[i], L[i])

print(max(DP))




# 누적합으로 풀면 시간 초과가 나요
# import sys
# input = sys.stdin.readline

# N = int(input())
# input_L = list(map(int,input().strip().split()))
# L = [0]

# for i in range(1,N+1,1):
#     tmp = input_L[i-1]
#     L.append(tmp+L[i-1])

# result = max(L[1:])

# for i in range(1,N+1,1):
#     for j in range(i-1, -1, -1):
#         result = max(L[i]-L[j], result)

# print(result)
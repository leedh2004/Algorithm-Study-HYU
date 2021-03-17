import sys
input = sys.stdin.readline

N = int(input())
max_N = 10001
L = [0 for _ in range(max_N)]

for i in range(N):
    L[i] = int(input())

if N == 1 :
    print(L[0])
    exit(0)

DP = [0 for _ in range(max_N)]
DP[0],DP[1] = L[0], L[0]+L[1]
DP[2] = max(L[0]+L[1],L[0]+L[2],L[1]+L[2])
DP[3] = max(L[0]+L[1]+L[3], L[0]+L[2]+L[3])

for i in range(4, N, 1):
    DP[i] = max(DP[i-3]+L[i-1]+L[i], DP[i-2]+L[i], DP[i-4]+L[i-1]+L[i])

# print(L[:7])
# print(DP[:7])
print(max(DP[N-2],DP[N-1]))



# 6
# 100
# 100
# 1
# 1
# 100
# 100
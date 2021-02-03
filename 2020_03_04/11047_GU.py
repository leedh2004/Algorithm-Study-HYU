import sys

N,K = map(int,sys.stdin.readline().split())
A = [0] * N
for i in range(N):
    A[i] = int(sys.stdin.readline())
cnt = 0

for i in range(N-1,-1,-1):
    if A[i] <= K:
        cnt += (K//A[i])
        K %= A[i]
        if K == 0:
            break

print(cnt)


import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
d = [0 for _ in range(N)]
for i in range(N):
    maximum = 0
    for j in range(i):
        if (A[i] > A[j] and maximum <d[j]):
            maximum = d[j]
    d[i] = maximum +1
print(max(d))

import sys

N = int(sys.stdin.readline())
d = [0 for _ in range(N+1)]
A=list(map(int,sys.stdin.readline().split()))
A.insert(0,0)
maximum = 0

for i in range(1,N+1):
    d_max = 0
    for j in range(i):
        if (A[i] > A[j]):
            if(d_max <d[j]):
                d_max = d[j]
    d[i] = d_max + A[i]
    if(maximum < d[i]):
        maximum = d[i]

print(maximum)
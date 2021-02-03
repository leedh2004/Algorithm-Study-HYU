import sys
N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))
A.insert(0,0)
maximum=0
d = [0 for _ in range(N+1)]

for i in range(1,N+1):
    minimum = 0
    for j in range(i):
        if (A[i] > A[j]):
            if(minimum <d[j]):
                minimum = d[j]
    d[i] = minimum +1
    if(maximum < d[i]):
        maximum = d[i]
print(maximum)
#

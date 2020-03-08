import sys

N = int(sys.stdin.readline())

A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

A.sort(key = lambda x:x[0])
A.insert(0,[0,0])

d = [0 for _ in range(N+1)]
maximum = 0

for i in range(1,N+1):
    minimum = 0
    for j in range(i):
        if(A[i][1] > A[j][1]):
            if(minimum < d[j]):
                minimum = d[j]
    d[i] = minimum + 1
    if(maximum < d[i]):
        maximum = d[i]
print(N-maximum)

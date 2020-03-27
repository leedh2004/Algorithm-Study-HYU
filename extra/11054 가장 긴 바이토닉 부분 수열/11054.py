import sys

N = int(sys.stdin.readline())
A= list(map(int,sys.stdin.readline().split()))
A.insert(0,0)

d = [[0]*2 for _ in range(N+1)]

for i in range(1,N+1):
    minimum = 0
    for j in range(i):
        if(A[i] > A[j]):
            if(minimum < d[j][0]):
                minimum = d[j][0]
    d[i][0] = minimum + 1 
for i in range(N,-1,-1):
    minimum = 0
    for j in range(N,i,-1):
        if(A[i] > A[j]):
            if(minimum < d[j][1]):
                minimum = d[j][1]
    d[i][1] = minimum +1
maximum = 0
for i in range(1,N+1):
    if(maximum < d[i][0] + d[i][1]):
        maximum = d[i][0] + d[i][1]

print(maximum -1)

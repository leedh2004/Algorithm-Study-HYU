import sys

N = int(sys.stdin.readline())

d = [[0]*3 for _ in range(N+1)]

for i in range(1,N+1):
    d[i][0] = int(sys.stdin.readline())
    d[i][1] = d[i][0]
    d[i][2] = d[i][0]
    if(i==1):
        d[i][0]=0
        d[i][2]=0
    elif(i==2):
        d[i][0] = d[i-1][1]
        d[i][2] += d[i-1][1]
    
for i in range(3,N+1):
    d[i][0] = max(d[i-1][1],d[i-1][2])
    d[i][1] += d[i-1][0]
    d[i][2] += d[i-1][1]

print(max(d[N][0],d[N][1],d[N][2]))

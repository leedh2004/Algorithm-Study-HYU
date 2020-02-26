import sys

N = int(sys.stdin.readline())

d = [[int(sys.stdin.readline())]*2 for _ in range(N)]
if(N==1):
    print(d[0][1])
elif(N==2):
    print(d[0][1]+d[1][0])

d[0][0] = -1
d[1][1] = d[0][1] + d[1][0]
for i in range(2,N):
    d[i][0] += max(d[i-2][0],d[i-2][1])
    d[i][1] += d[i-1][0]
print(d)
if(N!=1 and N!=2):
    print(max(d[N-1][0],d[N-1][1]))

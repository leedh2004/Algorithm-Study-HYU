import sys

N = int(sys.stdin.readline())

if(N < 1 or N > 100):
    sys.exit(1)
d = [[0]*(11) for _ in range(N+1)]

for i in range(1,10):
    d[1][i] = 1
for i in range(2,N+1):
    d[i][0] = d[i-1][1] %1000000000
    for j in range(1,9):
        d[i][j] = (d[i-1][j-1] + d[i-1][j+1])%1000000000
    d[i][9] = d[i-1][8] %1000000000
cnt = 0
for i in range(10):
    cnt = (cnt+d[N][i])%1000000000
print(cnt%1000000000)
    


import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    up = list(map(int,sys.stdin.readline().split()))
    down = list(map(int,sys.stdin.readline().split()))
    d = [[0,0] for _ in range(n+1)]
    d[1][0] = up[0]
    d[1][1] = down[0]
    res = 0
    for j in range(2,n+1): # 0 up 1 down
        d[j][0] = max(d[j-2][1] + up[j-1], d[j-1][1] + up[j-1])
        d[j][1] = max(d[j-2][0] + down[j-1], d[j-1][0] + down[j-1])
        res = max(d[j][0],d[j][1])
    print(res)
    
    
import sys
INF = sys.maxsize
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    cur_x, cur_y = map(int,sys.stdin.readline().split())
    P = [[cur_x,cur_y]]
    for j in range(n):
        pyeon = list(map(int,sys.stdin.readline().split()))
        P.append(pyeon)
    r_x, r_y = map(int,sys.stdin.readline().split())
    P.append([r_x,r_y])
    dist = []
    for j in range(n+2):
        tmp = [0 for _ in range(n+2)]
        for k in range(n+2):
            tmp[k] = abs(P[j][0] - P[k][0]) + abs(P[j][1] - P[k][1])
            if tmp[k] > 1000:
                tmp[k] = INF
        tmp[j] = 0
        dist.append(tmp)
    for j in range(n+2):
        for k in range(n+2):
            for l in range(n+2):
                if dist[k][j] + dist[j][l] < dist[k][l]:
                    dist[k][l] = dist[k][j] + dist[j][l]
    if dist[0][n+1] != INF: print("happy")
    else: print("sad")
    
    
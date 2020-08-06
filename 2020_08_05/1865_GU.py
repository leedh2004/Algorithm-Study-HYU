import sys

#웜홀의 도착지 X개 -> 벨만포드 X번 (X)
#시작지점 임의로 두고 벨만포드 -> 음수 사이클 확인 (O)

INF = sys.maxsize
input = sys.stdin.readline

TC = int(input())
for i in range(TC):
    N,M,W = map(int,input().split())
    d = [INF] * (N+1)
    #파이썬에서 벡터 대용으로 일단 이렇게 썼음
    edges =[[]*(N+1) for _ in range(N+1)]
    for j in range(M):
        a,b,c = map(int,input().split())
        #방향 X (양방향)
        edges[a].append([b,c])
        if a == b: continue
        edges[b].append([a,c])
    for j in range(W):
        a,b,c = map(int,input().split())
        edges[a].append([b,-c])
    #1을 출발 지점으로
    d[1] = 0
    cycle = False

    #N번 반복, 마지막에 또 갱신 된다 -> 음수 cycle
    for j in range(1,N+1):
        #k -> 출발지
        for k in range(1,N+1):
            for x in range(len(edges[k])):
                dest = edges[k][x][0]
                time = edges[k][x][1]

                if d[dest] > d[k] + time:
                    d[dest] = d[k] + time
                    if j == N: cycle = True
 
    if cycle: print("YES")
    else: print("NO")
    

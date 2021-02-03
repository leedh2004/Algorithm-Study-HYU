import sys

INF = sys.maxsize
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 앞의 물건이 뒤의 물건보다 더 무겁다
dist = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    f, t = map(int, sys.stdin.readline().split())
    dist[f][t] = 1

# 거쳐가는 노드
for i in range(1, N+1):
    # 시작 노드
    for j in range(1, N+1):
        # 도착 노드
        for k in range(1, N+1):
            if dist[j][k] > dist[j][i] + dist[i][k]:
                # dist[j][k] = dist[j][i] + dist[i][k]
                dist[j][k] = 1

for i in range(1, N+1):
    ans = 0
    for j in range(1, N+1):
        if dist[i][j] == INF and dist[j][i] == INF:
            ans += 1
    print(ans-1)

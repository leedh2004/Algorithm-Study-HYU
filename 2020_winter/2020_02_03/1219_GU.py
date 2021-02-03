import sys


def check(a):
    if a == e:
        return True
    visited = [False for _ in range(N)]
    visited[a] = True
    q = [a]
    for i in range(len(graph[a])):
        q.append(graph[a][i][0])

    while q:
        dest = q.pop(0)
        if not visited[dest]:
            if dest == e:
                return True
            else:
                visited[dest] = True
                for i in range(len(graph[dest])):
                    q.append(graph[dest][i][0])

    return False


INF = sys.maxsize
N, s, e, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, -c])

earn = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    for j in range(len(graph[i])):
        graph[i][j][1] += earn[graph[i][j][0]]
# print(graph)
d = [-INF for _ in range(N)]
d[s] = earn[s]

for i in range(N-1):
    for start in range(N):
        for k in range(len(graph[start])):
            dest, cost = graph[start][k]
            if d[dest] < d[start] + cost and d[start] != -INF:
                d[dest] = d[start] + cost
if d[e] == -INF:
    print("gg")
else:
    cycle = False
    has_cycle = []
    for start in range(N):
        for k in range(len(graph[start])):
            dest, cost = graph[start][k]
            if d[dest] < d[start] + cost and d[start] != -INF:
                #d[dest] = d[start] + cost
                cycle = True
                has_cycle.extend([start, dest])
    if not cycle:
        print(d[e])
    else:
        if has_cycle:
            has_cycle = list(set(has_cycle))
        # 하나라도 도달하는 cycle 있으면 Gee가 되어야 한다.
        # 사이클은 여러개 존재할 수 있다.
        Gee = False
        for i in range(len(has_cycle)):
            if check(has_cycle[i]):
                # print(d[e])
                Gee = True

        # 틀린 코드 !!!!!!!!!!!!!!!!!!!!!!!!
        # Gee = True
        # for i in range(len(has_cycle)):
        #     if not check(has_cycle[i]):
        #         # print(d[e])
        #         Gee = False
        #         break

        if Gee:
            print("Gee")
        else:
            print(d[e])

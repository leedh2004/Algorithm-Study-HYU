from heapq import heappush, heappop
import sys

INF = sys.maxsize


def dij(start):
    d = {i: INF for i in range(1, V+1)}
    d[start] = 0
    q = []
    heappush(q, [d[start], start])

    while q:
        dist, cur = heappop(q)

        if d[cur] < dist:
            continue

        for new_dist, dest in adj_list[cur]:
            distance = dist + new_dist
            if distance < d[dest]:
                d[dest] = distance
                heappush(q, [distance, dest])

    return d


V, E = map(int, sys.stdin.readline().split())
adj_list = {}
for i in range(1, V+1):
    adj_list[i] = []
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj_list[u].append([w, v])
    adj_list[v].append([w, u])
maam = list(map(int, sys.stdin.readline().split()))
start = int(sys.stdin.readline())

my_dij = dij(start)
answers = []
maam_time = 0

maam_cur = maam[0]
if start == maam_cur:
    answers.append(start)
for i in range(1, 10):
    maam_dest = maam[i]
    maam_dij = dij(maam_cur)
    if maam_dij[maam_dest] == INF:
        continue
    maam_time += maam_dij[maam_dest]
    if maam_time >= my_dij[maam_dest]:
        answers.append(maam_dest)
    maam_cur = maam_dest

if not answers:
    print(-1)
else:
    print(min(answers))

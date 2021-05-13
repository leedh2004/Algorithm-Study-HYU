from collections import deque
import sys


def solution(n, start, end, roads, traps):
    answer = 0
    result = sys.maxsize
    q = deque([[start, 0, 0]])
    d1 = {i: [] for i in range(1, n+1)}
    d2 = {i: [] for i in range(1, n+1)}
    for i in range(len(roads)):
        d1[roads[i][0]].append([roads[i][1], roads[i][2]])
    for i in range(len(roads)):
        if roads[i][1] not in traps:
            d2[roads[i][0]].append([roads[i][1], roads[i][2]])
        else:
            d2[roads[i][1]].append([roads[i][0], roads[i][2]])
    visited1 = [False for _ in range(1, n+1)]
    visited2 = [False for _ in range(1, n+1)]
    visited1[start] = True

    while q:
        cur, d_idx, time = q.popleft()
        if cur == end:
            result = min(result, time)
            continue
        if not d_idx:
            d = d1
        else:
            d = d2
        for i in range(len(d[cur])):
            if d[cur][i]:
                if d[cur][i][0] in traps:
                    q.append([d[cur][i][0], abs(1-d_idx), time+d[cur][i][1]])
                else:
                    q.append([d[cur][i][0], d_idx, time+d[cur][i][1]])

    return result

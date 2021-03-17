import sys
from collections import deque


T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
    print(N-1)
    # flight = {}
    # for i in range(N):
    #     flight[i+1] = []
    # for i in range(M):
    #     a, b = map(int, sys.stdin.readline().split())
    #     flight[a].append(b)
    #     flight[b].append(a)

    # # BFS
    # cnt = 0
    # q = deque([1])
    # visited = [False for i in range(N+1)]
    # visited[1] = True

    # while q:
    #     cnt += 1
    #     for i in range(len(q)):
    #         cur = q.popleft()
    #         for dest in flight[cur]:
    #             if not visited[dest]:
    #                 q.append(dest)
    #                 visited[dest] = True
    # print(cnt)

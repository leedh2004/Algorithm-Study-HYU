import sys
from collections import deque
a, b = map(int, sys.stdin.readline().split())
N, M = map(int, sys.stdin.readline().split())

ways = {}
for i in range(N):
    ways[i+1] = []
for _ in range(M):
    e, f = map(int, sys.stdin.readline().split())
    ways[e].append(f)
    ways[f].append(e)
visited = [False for _ in range(N+1)]
visited[a] = True
q = deque([a])
cnt = 0
flag = False
while q:
    cnt += 1
    for _ in range(len(q)):
        cur = q.popleft()
        if cur == b:
            print(cnt-1)
            flag = True
            break
        for dest in ways[cur]:
            if not visited[dest]:
                q.append(dest)
                visited[dest] = True
    if flag:
        break
if not flag:
    print(-1)

import sys
input = sys.stdin.readline
from collections import deque

a,b = map(lambda x : int(x)-1, input().split())

if a ==  b :
    print(0)
    exit(0)

N,M = map(int,input().split())
adj = {i : [] for i in range(N)}

for i in range(M):
    s,e = map(lambda x : int(x)-1, input().split())
    adj[s].append(e)
    adj[e].append(s)

q = deque([a])
visit = [False for _ in range(N)]
visit[a] = True
result = 0

while q :
    result += 1
    for i in range(len(q)):
        tar = q.popleft()
        for j in adj[tar] :
            if visit[j] == False :
                if j == b :
                    print(result)
                    exit(0)
                visit[j] = True
                q.append(j)

print(-1)
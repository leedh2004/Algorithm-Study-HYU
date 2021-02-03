import collections
N = int(input())
result = [0 for _ in range(N+1)]
adj = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]

for i in range(N-1):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

q = collections.deque()
q.append(1)
visit[1] = True

while q :
    t = q.popleft()
    for i in adj[t] :
        if visit[i] == False :
            visit[i] = True
            result[i] = t
            q.append(i)

for i in range(2,N+1,1):
    print(result[i])
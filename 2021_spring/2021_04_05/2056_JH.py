import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
indegree = [0 for _ in range(N)]
next_node = {i:[] for i in range(N)}
cost = [0 for _ in range(N)]
q = deque()
DP = [0 for _ in range(N)]

for i in range(N):
    sentence = list(map(int,input().strip().split()))
    cost[i], indegree[i] = sentence[0], sentence[1]
    for j in range(2,2+sentence[1]):
        idx = sentence[j]-1
        next_node[idx].append(i)

for i in range(N):
    if indegree[i] == 0 :
        q.append(i)
        indegree[i] = -1
        # DP[i] = cost[i]


while q :
    t = q.popleft()
    DP[t] += cost[t]
    for j in next_node[t]:
        indegree[j] -= 1
        DP[j] = max(DP[j],DP[t])
        if indegree[j] == 0 :
            indegree[j] = -1
            q.append(j)
            
print(max(DP))
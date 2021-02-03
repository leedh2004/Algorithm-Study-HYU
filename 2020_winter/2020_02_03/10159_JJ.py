import sys

# 입력
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dist = [[False for _ in range(n)] for _ in range(n)]
indegree = [0 for _ in range(n)]
outdegree = [0 for _ in range(n)]
for i in range(m):
  st,ed = map(int,sys.stdin.readline().split())
  if not dist[st-1][ed-1]:
    dist[st-1][ed-1] = True
    outdegree[st-1] = outdegree[st-1] + 1
    indegree[ed-1] = indegree[ed-1] + 1
# 플로이드 와샬
for i in range(n):
  for j in range(n):
    if i==j:
      continue
    if not dist[j][i]:
        continue
    for k in range(n):
      if i==k or j==k or not dist[i][k] :
        continue
      if dist[j][i] and dist[i][k] and not dist[j][k]:
        dist[j][k] = True
        outdegree[j] =  outdegree[j] + 1
        indegree[k] = indegree[k] + 1

for i in range(n):
  # 전체 노드 수 - (현재 노드보다 작은 노드 + 현재 노드보다 큰 노드 + 현재 노드)
  print(n-(outdegree[i]+indegree[i]+1))

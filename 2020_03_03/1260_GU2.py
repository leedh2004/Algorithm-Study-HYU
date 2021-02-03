import sys

def dfs(graph,v,cnt):
    if visited[v] == True:
        return
    cnt += 1
    print(v,end=' ')
    visited[v] = True
    child = []
    for i in range(len(graph[v])):
        if(graph[v][i] == 1):
            dfs(graph,i,cnt)


N, M, v = map(int,sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
for k in range(M):
    i,j = map(int,sys.stdin.readline().split())
    graph[i][j] = 1
    graph[j][i] = 1
     
visited = [False] * (N+1)

dfs(graph,v,0)
print()

visit = []
queue = [v,]

while queue:
    node = queue.pop(0)
    if node not in visit:
        visit.append(node)
        for i in range(len(graph[node])):
            if graph[node][i] == 1:
                queue.append(i)
for i in range(len(visit)):
    print(visit[i],end=' ')


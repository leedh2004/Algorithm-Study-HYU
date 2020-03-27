import sys

def dfs(graph,v):
    stack = [v,]
    visited = [False] * N
    cnt = 0
    while True:
        if len(stack) == 0:
            break
        node = stack.pop()
        cnt += 1
        visited[node-1] = True
        if cnt != N:
            print(node, end=' ')
        else:
            print(node)
        child = []
        for i in range(len(graph)):
            if(graph[i][0] == node and visited[graph[i][1]-1] == False):
                child.append(graph[i][1])
        if len(child) != 0:
            stack.append(min(child))
        

def bfs(graph,v):
    visited = [False] * N
    queue = [v,]
    cnt = 0
    while True:
        if len(queue) == 0:
            break
        node = queue.pop(0)
        visited[node-1] = True
        if cnt != N:
            print(node, end=' ')
        else:
            print(node)
        child = []
        for i in range(len(graph)):
            if(graph[i][0] == node and visited[graph[i][1]-1] == False):
                child.append(graph[i][1])
        child.sort()
        if(len(child)==0):
            break
        for i in range(len(child)):
            queue.append(child[i])

N, M, v = map(int,sys.stdin.readline().split())
graph = []
for i in range(M):
    v_1, v_2 = map(int,sys.stdin.readline().split())
    graph.append((v_1,v_2))
    graph.append((v_2,v_1))
dfs(graph,v)
bfs(graph,v)
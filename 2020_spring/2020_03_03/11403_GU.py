import sys

def dfs(adj, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)
    first = True
    while stack:
        node = stack.pop()
        if node not in visit and first ==False:
            visit.append(node)
            stack.extend(adj[node])
        elif node not in visit and first:
            stack.extend(adj[node])
            first = False

    for i in range(len(visit)):
        result[start_node][visit[i]] = 1

N = int(sys.stdin.readline())
adj = dict()
result = [[0]*N for _ in range(N)]
for i in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    value = []
    for j in range(N):
        if(line[j] == 1):
            value.append(j)
            result[i][j]= 1
    adj[i] = value

for i in range(N):
    dfs(adj,i)

for i in range(N):
    line = result[i]
    for j in range(N):
        print(line[j],end =' ')
    print()

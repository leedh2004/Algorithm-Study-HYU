import sys
import copy
def dfs(adj, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)
    
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(adj[node])
    
    return visit

N,M = map(int,sys.stdin.readline().split())
adj = dict()
link = []
for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    link.append((u,v))
    link.append((v,u))
link.sort(key = lambda x:x[0])

value =[]

for i in range(N):
    value =[]
    for (x,y) in link:
        if x== i+1:
            value.append(y)
    value_ = copy.deepcopy(value)
    adj[i+1] = value_

done =[]
cnt = 0
for i in range(1,N+1):
    if i not in done:
        done.extend(dfs(adj,i))
        cnt+=1
print(cnt)
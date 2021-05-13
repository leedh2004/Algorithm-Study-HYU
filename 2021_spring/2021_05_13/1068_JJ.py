import sys

input = sys.stdin.readline

def dfs(node):

    # 이미 존재할 때
    if leafs[node]:
        return leafs[node]
    
    # leaf node 일때
    elif len(adj[node])==0:
        leafs[node] = 1
        return 1
    
    leafNum = 0
    for i in range(len(adj[node])):
        leafNum = leafNum + dfs(adj[node][i])

    leafs[node] = leafNum
    return leafNum


n = int(input())
p = list(map(int,input().split()))
adj = [[] for _ in range(n)]
root = None
leafs = [0 for _ in range(n)]
for i in range(n):
    if p[i] == -1:
        root = i
    else :
        adj[p[i]].append(i)

dfs(root)
m = int(input())
# root를 지우려고 할때
if root==m:
    print(0)
# 지운 노드의 부모 노드가 leaf 가 되는 경우
elif leafs[m] == leafs[p[m]]:
    print(leafs[root]-leafs[m]+1)
else :
    print(leafs[root]-leafs[m])
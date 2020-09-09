import sys
sys.setrecursionlimit(2500)

def dfs(t,tmp):
    global N, adj, visit, result
    visit[t] = True
    if tmp == 4:
        result = True
        return 
    for i in adj[t] :
        if visit[i] == False :
            dfs(i,tmp+1)
            visit[i] = False

N, M = map(int,input().split())
adj = [[] for _ in range(N)]
visit = [False for _ in range(N)]
result = False

for i in range(M):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(N):
    if result :
        break
    if visit[i] == False :
        dfs(i,0)
        visit[i] = False  #더 적은 수가 트리에서 위를 차지한다는 보장이 없으므로
            
if result :
    print(1)
else :
    print(0)
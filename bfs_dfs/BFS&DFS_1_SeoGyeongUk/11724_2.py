import sys
sys.setrecursionlimit(100000)
def dfs(link,v):
    visit[v-1] = True
    for i in range(M):
        if(link[i][0]==v and visit[link[i][1]-1]==False):
            dfs(link,link[i][1])
        elif(link[i][1]==v and visit[link[i][0]-1]==False):
            dfs(link,link[i][0])

N,M = map(int,sys.stdin.readline().split())
link = []
for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    link.append([u,v])

visit =[False]*N
cnt = 0
for i in range(1,N+1):
    if not visit[i-1]:
        dfs(link,i)
        cnt+=1
    
print(cnt)
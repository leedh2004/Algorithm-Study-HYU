import sys
sys.setrecursionlimit(10**6)
N, M = map(int,input().split())
mat = [[0]*N for _ in range(N)]
visit = [False]*N
count = 0

def dfs(x) :
    global N
    visit[x] = True
    for i in range(N):
        if mat[x][i] == 1 and visit[i] == False:
            dfs(i)


for i in range(M) :
    a,b = map(int, input().split())
    mat[a-1][b-1] = 1
    mat[b-1][a-1] = 1

for j in range(N):
    for k in range(N):
        if mat[j][k] == 1 and visit[k] == False:
            dfs(j)    #dfs 한번 실행되면 연결요소 하나를 찾는거임
            count += 1

result = len(list(filter(lambda x: x==False,visit))) + count
print(result)
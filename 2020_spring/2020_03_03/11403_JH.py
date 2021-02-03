N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]

def dfs(N,mat,visit,x):
    for i in range(N):
        if mat[x][i] == 1 and visit[i] == 0 :
            visit[i] = 1
            dfs(N,mat,visit,i)


for i in range(N):
    visit = [0]*N
    dfs(N,mat,visit,i)  #한번 실행 될떄 한점에서 어느점들을 갈 수 있는지 visit에 찍을꺼임
    for j in range(N):
        if visit[j] == 1 :
            print(1, end = ' ')
        elif visit[j] == 0 :
            print(0, end = ' ')
    print()
import copy
def dfs(x,y,tmp,count,visit):
    global N, mat,result, dx, dy
    visit[x][y] = True
    tmp += mat[x][y]
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N or visit[nx][ny] == True :
            return
        visit[nx][ny] = True
        tmp += mat[nx][ny]

    if count == 3:
        result = min(result, tmp)
        return 

    for i in range(x,N-1):
        for j in range(0,N-1):
            if(visit[i][j]==False):
                dfs(i,j,tmp,count+1,copy.deepcopy(visit))

    
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
visit = [[False for _ in range(N)] for i in range(N)]
result = 1e9
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(1,N-1,1):
    for j in range(1,N-1,1):
        dfs(i,j,0,1,copy.deepcopy(visit))

print(result)
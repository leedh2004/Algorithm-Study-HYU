import sys

dy = [1,0,-1,0]
dx = [0,1,0,-1]

def inRange(y,x):
    return (y>=0 and y<=N-1) and (x>=0 and x<=N-1)

def bfs(r,c,visit):
    q = [[r,c]]
    visit[r][c] = True
    cnt = 0
    while q:
        [y,x] = q.pop(0)
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(inRange(ny,nx) and A[ny][nx] != 0 and visit[ny][nx]==False):
                visit[ny][nx] = True
                q.append([ny,nx])
    return cnt


N = int(sys.stdin.readline())
A = [[0]*N for _ in range(N)]
visit = [[False]*N for _ in range(N)]

for i in range(N):
    line = sys.stdin.readline()
    for j in range(N):
        if(line[j]== '1'):
            A[i][j] =1
housing = 0
housing_cnt = []
for i in range(N):
    for j in range(N):
        if(A[i][j]== 1 and visit[i][j]== False):
            housing_cnt.append(bfs(i,j,visit))
            housing +=1
housing_cnt.sort()
print(housing)
for i in range(len(housing_cnt)):
    print(housing_cnt[i])


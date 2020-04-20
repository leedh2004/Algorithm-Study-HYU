import collections      #visit배열 없어도 됨 ??

def check_R(nx,ny,N):
    if nx>=0 and nx<N and ny>=0 and ny<N:
        return True
    else :
        return False

def bfs(N,mat):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = collections.deque()
    q.append((0,0))
    cost = [[9999]*N for _ in range(N)]
    cost[0][0] = mat[0][0]

    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if check_R(nx,ny,N)  and cost[x][y]+mat[nx][ny] < cost[nx][ny] :
                q.append((nx,ny))
                cost[nx][ny] = cost[x][y]+mat[nx][ny]
    return cost[N-1][N-1]


if __name__ == '__main__':
    count = 1
    while True:
        N = int(input())
        if N == 0 :
            break
        mat = [list(map(int,input().split())) for _ in range(N)]
        print("Problem %d: %d" %(count,bfs(N,mat)))
        count+=1

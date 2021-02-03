import collections  #부등호 하나 잘못 써서 2시간 봤어용 ㅎ
def bfs(x,y):
    global N, mat, shark_size, hungry, result, food
    ret_x, ret_y = 100, 100
    tmp_time = 1
    add_time = 500
    dx, dy = [-1,0,1,0], [0,-1,0,1]
    visit  = [ [False for _ in range(N)] for i in range(N) ]
    visit[x][y] = True
    q = collections.deque()
    q.append([x,y])
    while q :
        for j in range(len(q)) :
            x,y = q.popleft()
            # print("x:",x,"y:",y)
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                # print("nx:1",nx,"ny1:",ny)
                if nx>=0 and nx<N and ny>=0 and ny<N and visit[nx][ny] == False and mat[nx][ny] <= shark_size :
                    if mat[nx][ny] < shark_size and mat[nx][ny] != 0 :
                        if add_time >= tmp_time :
                            add_time = tmp_time
                            if add_time == tmp_time :
                                if ret_x == nx and ret_y > ny :
                                    ret_y = ny
                                elif ret_x > nx :
                                    ret_x, ret_y = nx, ny
                    q.append([nx,ny])
                    visit[nx][ny] = True
        tmp_time += 1
    # print(ret_x,ret_y,add_time,shark_size)
    if ret_x != 100 and ret_y != 100 :
        hungry += 1
        food -= 1
        if hungry == shark_size :
            hungry = 0
            shark_size += 1
        result += add_time
        mat[ret_x][ret_y] = 0
        # print(mat)
        # print(ret_x,ret_y,add_time,shark_size,hungry)
        return ret_x, ret_y
    return ret_x, ret_y


def solve(x,y):
    global result, food
    while True :
    # for i in range(40):
        # print("start bfs")
        x,y = bfs(x,y)
        if (food == 0) or (x == 100 and y == 100) :
            print(result)
            return

N = int(input())
mat = [ list(map(int,input().split())) for _ in range(N) ]
start_x, start_y = 0,0
shark_size = 2
hungry = 0
result = 0
food = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] == 9 :
            start_x, start_y = i,j
            mat[i][j] = 0
        elif mat[i][j] != 0 and mat[i][j] != 9 :
            food += 1

solve(start_x,start_y)
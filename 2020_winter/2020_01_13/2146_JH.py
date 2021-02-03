from collections import deque

N = int(input())
mat = [ list(map(int,input().split())) for _ in range(N) ]
result = 300
numbering = 1

def seperate(ori_x, ori_y):
    global N, mat, numbering
    numbering += 1
    # print("first, ",ori_x, ori_y, numbering)
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    visit = [ [False for _ in range(N)] for i in range(N) ] 
    q = deque()
    q.append([ori_x, ori_y])
    visit[ori_x][ori_y] = True
    mat[ori_x][ori_y] = numbering

    while q :
        for j in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if nx>=0 and nx<N and ny>=0 and ny<N and visit[nx][ny] == False and mat[nx][ny] == 1 :
                    q.append([nx, ny])
                    visit[nx][ny] = True
                    mat[nx][ny] = numbering
                    # print(nx, ny, mat[nx][ny])

    # for line in mat :
    #     print(line)
    # exit(0)

def solution(ori_x, ori_y, my_num):
    global N, mat, result
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    
    flag = True
    for i in range(4):
        nx,ny = ori_x+dx[i], ori_y+dy[i]
        if nx>=0 and nx<N and ny>=0 and ny<N and mat[nx][ny] != my_num :
            flag = False
            break
    if flag :
        return result
        
    visit = [ [False for _ in range(N)] for i in range(N) ] 
    q = deque()
    q.append([ori_x, ori_y])
    visit[ori_x][ori_y] = True

    depth = -1

    while q :
        depth += 1
        for j in range(len(q)):
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if nx>=0 and nx<N and ny>=0 and ny<N and visit[nx][ny] == False :
                    if mat[nx][ny] != my_num :
                        if mat[nx][ny] != 0 :
                            return depth
                        else :
                            q.append([nx, ny])
                            visit[nx][ny] = True
    return 300

for i in range(N):
    for j in range(N):
        if mat[i][j] == 1 :
            seperate(i,j)

for i in range(N):
    for j in range(N):
        if mat[i][j] != 0 :
            # tmp = solution(i,j,mat[i][j])
            # if (tmp < result) : 
                # print(i,j)
            result = min(result, solution(i,j, mat[i][j]))

print(result)

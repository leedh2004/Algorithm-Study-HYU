def solve(N,x,y) :
    global count0, count1, count2
    if N == 1 :
        if mat[x][y] == 0 :
            count0 += 1
        elif mat[x][y] == 1 :
            count1 += 1
        elif mat[x][y] == -1 :
            count2 += 1
        return 
    flag = True
    for i in range(N) : 
        nx = x+i
        if flag == True :
            for j in range(N):
                ny = y+j
                if mat[x][y] != mat[nx][ny] :
                    flag = False
                    solve(N//3,x,y)
                    solve(N//3,x,y+N//3)
                    solve(N//3,x,y+2*N//3)
                    solve(N//3,x+N//3,y)
                    solve(N//3,x+N//3,y+N//3)
                    solve(N//3,x+N//3,y+2*N//3)
                    solve(N//3,x+2*N//3,y)
                    solve(N//3,x+2*N//3,y+N//3)
                    solve(N//3,x+2*N//3,y+2*N//3)
                    break
    if flag :
        if mat[x][y] == 0 :
            count0 += 1
        elif mat[x][y] == 1 :
            count1 += 1
        elif mat[x][y] == -1 :
            count2 += 1

N = int(input())
mat = [ list(map(int, input().split())) for _ in range(N) ]
count0, count1, count2 = 0,0,0
solve(N,0,0)
print(count2)
print(count0)
print(count1)
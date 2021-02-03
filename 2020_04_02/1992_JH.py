N = int(input())  #ㅠㅠ 모르겠어용....
mat = [list(str(input())) for _ in range(N) ]
result =""

def solve(N,M,x,y):
    global result
    flag = True
    if N == 1 or M == 1:
        return str(mat[x][y])
    
    else :
        for i in range(x,N,1):
            now = mat[x][y]
            for j in range(y,M,1):
                if mat[i][j] != now :
                    flag = False
                    result += "("
                    result += solve(N//2,M//2,x,y)  #왼쪽 위
                    result +=")"

                    result += "("
                    result += solve(N//2,M,x,N//2) #오른쪽 위
                    result +=")"

                    result += "("
                    result += solve(N,M//2,N//2,y) #왼쪽 아래
                    result +=")"

                    result += "("
                    result += solve(N,M,N//2,N//2) #오른쪽 아래
                    result +=")"
        if flag == True :
            return str(mat[x][y])

solve(N,N,0,0)
print(result)
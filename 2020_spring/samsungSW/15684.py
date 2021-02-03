import sys

def check(A,N,H):
    for i in range(1,N+1):
        cur = i

        for j in range(1,H+1):
            if(A[j][cur] == True): cur +=1
            elif(A[j][cur-1] == True): cur -=1
        
        if(i != cur): return False

    return True
                        
def dfs(cnt,x,y):
    global A,N,H,ret
    if(cnt >= ret):
        return
    if(check(A,N,H)):
        ret = cnt
        return
    if (cnt == 3):
        return
    for i in range(y,H+1):
        for j in range(x,N):
            if(A[i][j]):
                j+= 1
                continue
            A[i][j] = True
            dfs(cnt+1,j+2,i)
            A[i][j] = False
        x=1


N,M,H = map(int,sys.stdin.readline().split())
A = [[False]*(N+1) for _ in range(H+1)]
before =[[False]*(N+1) for _ in range(H+1)]


for i in range(M):
    r,c = map(int,sys.stdin.readline().split())
    A[r][c] = True

ret = 100000

dfs(0,1,1)

if(ret>3):
    print(-1)
else:
    print(ret)

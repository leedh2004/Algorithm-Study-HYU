import sys
sys.setrecursionlimit(100000)

ans = 0
M,N = None,None
table = None
dp = None

def recursive(x,y):
    global M,N,ans,dp
    
    # 범위 나가거나 장애물
    if x>M-1 or y>N-1:
        return 0    
    
    # 도착
    if x == M-1 and y == N-1:
        return 1
    
    # 메모제이션이 존재할때
    if dp[y][x] != -1:
        return dp[y][x]
    

    dp[y][x] = (recursive(x+1,y) + recursive(x,y+1)) % 1000000007
    
    return dp[y][x]

def solution(m, n, puddles):
    
    # 선언
    global ans,M,N,table,dp
    M,N=m,n
    table = [[-1 for col in range(m)] for row in range(n)]
    dp = [[-1 for col in range(m)] for row in range(n)]
    
    # 장애물 테이블화
    for i in puddles:
        dp[i[1]-1][i[0]-1] = 0
        table[i[1]-1][i[0]-1] = 1
    
    recursive(0,0)

    
    return dp[0][0]
import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
visit = [ [ [False for i in range(101)] for j in range(101) ] for k in range(101) ]
DP = [ [ [0 for i in range(101)] for j in range(101) ] for k in range(101) ]
alpha = 50

def solution(a,b,c):
    global visit, DP, alpha
    idx_a, idx_b, idx_c = a+alpha, b+alpha, c+alpha

    if visit[idx_a][idx_b][idx_c] == True:
        return DP[idx_a][idx_b][idx_c]

    if a <= 0 or b <= 0 or c <= 0 :
        DP[idx_a][idx_b][idx_c] = 1
        visit[idx_a][idx_b][idx_c] = 1
        return 1

    if a>20 or b>20 or c>20 :
        DP[idx_a][idx_b][idx_c] = solution(20,20,20)
        visit[idx_a][idx_b][idx_c] = True
        return DP[idx_a][idx_b][idx_c]

    if a<b and b<c :
        DP[idx_a][idx_b][idx_c] = solution(a,b,c-1) + solution(a,b-1,c-1) - solution(a,b-1,c)
        visit[idx_a][idx_b][idx_c] = True
        return DP[idx_a][idx_b][idx_c]

    else :
        DP[idx_a][idx_b][idx_c] = solution(a-1,b,c) + solution(a-1,b-1,c) + solution(a-1,b,c-1) - solution(a-1,b-1,c-1)
        visit[idx_a][idx_b][idx_c] = True
        return DP[idx_a][idx_b][idx_c]


while a != -1 or b != -1 or c != -1 :
    result = solution(a,b,c)
    print("w(%d, %d, %d) = %d"%(a,b,c,result))
    a,b,c = map(int,input().split())
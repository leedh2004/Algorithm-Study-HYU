import sys
input = sys.stdin.readline

N = int(input())
cost = []
for i in range(N):
    cost.append( list(map(int,input().split())) )
INF = 10e20
result = INF

def solution(idx):
    global mat, cost, N, INF
    if idx == N :
        return

    mat[idx][0] = min( mat[idx-1][1]+cost[idx][0], mat[idx-1][2]+cost[idx][0]  )
    mat[idx][1] = min( mat[idx-1][0]+cost[idx][1], mat[idx-1][2]+cost[idx][1]  )
    mat[idx][2] = min( mat[idx-1][0]+cost[idx][2], mat[idx-1][1]+cost[idx][2]  )

    solution(idx+1)

for i in range(3):
    mat = [ [INF,INF,INF] for _ in range(N)  ] 
    mat[0][i] = cost[0][i]
    solution(1)
    for j in range(3):
        if i == j :
            continue
        result = min(result,mat[N-1][j])

print(result)

    


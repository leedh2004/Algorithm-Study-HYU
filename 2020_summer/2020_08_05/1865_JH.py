TC = int(input())

for i in range(TC):
    N, M, W  = map(int,input().split())
    mat = [[10001 for _ in range(N)] for _ in range(N) ]
    result = [10001 for _ in range(N)]
    flag = False
    
    for j in range(M):
        s,d,c = map(int,input().split())
        mat[s-1][d-1] = min(mat[s-1][d-1],c)  #도로는 양방향이니까
        mat[d-1][s-1] = min(mat[d-1][s-1],c)

    for j in range(W):
        s,d,c = map(int,input().split())
        mat[s-1][d-1] = min(mat[s-1][d-1],-c)

    for l in range(N+1):
        for j in range(N):
            for k in range(N):  #시작점이 정해져 있지 않고 임의의 한 지점만 가능해도 되니 음수 사이클이 있는지만 판명, 시작점에서 도달 가능한지 등 체크 x
                if result[k] > result[j]+mat[j][k]:
                    result[k] = result[j]+mat[j][k]
                    if l == N:
                        flag = True

    if(flag == True):
        print("YES")
    else :
        print("NO")
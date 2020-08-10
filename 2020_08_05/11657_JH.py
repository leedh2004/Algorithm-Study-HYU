N, M = map(int,input().split())
mat = [[10001*500 for _ in range(N)] for _ in range(N)]
result = [10001*500 for _ in range(N)]
result[0] = 0
flag = False

for i in range(M):
    s,d,c = map(int,input().split())
    mat[s-1][d-1] = min(mat[s-1][d-1],c)

for i in range(N):
    for j in range(N):
        # if(result[j]==10001):
        #     continue
        for k in range(N):
            if result[j] != 10001*500 and result[k] > result[j]+mat[j][k]:
                result[k] = result[j]+mat[j][k]
                if i == N-1 :
                    flag = True

if flag == True :
    print(-1)
else : 
    for i in range(1,N,1):
        if result[i] == 10001*500:
            print(-1)
        else :
            print(result[i])

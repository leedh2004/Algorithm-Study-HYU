#2458 - 키순서

N, M = map(int, input().split())
result = 0

mat = [ [500 for _ in range(500)] for i in range(500) ]

for i in range(M) :
    a, b = map(int, input().split())
    mat[a-1][b-1] = 1

for k in range(N) : 
    for i in range(N):
        for j in range(N):
            if(mat[i][j] > mat[i][k] + mat[k][j]):
                mat[i][j] = mat[i][k] + mat[k][j]

tmp = [0 for _ in range(N)]

for i in range(N) :
    for j in range(N) : 
        if mat[i][j] != 500 : 
            tmp[j] += 1 
            tmp[i] += 1

for i in range(N) : 
    if tmp[i] == N-1 :
        result +=1

print(result)
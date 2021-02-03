N, M = map(int,input().split())   #왜 틀린건지 모르겠습니다 ㅠ
mat = [list(str(input())) for _ in range(N)]
result = -1
for i in range(N):
    for j in range(M):
        tmp = j
        for k in range(j,M,1):
            if mat[i][k] == mat[i][j] :
                tmp = k
        
        length = tmp-j
        if i+length<N  :
            if mat[i][j] == mat[i+length][j] and mat[i][tmp] == mat[i+length][tmp] :
                result = max(result, length)
print((result+1)*(result+1))
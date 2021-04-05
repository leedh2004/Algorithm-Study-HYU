import sys
input = sys.stdin.readline

N,M = map(int, input().strip().split())
mat = [ list(input().strip()) for _ in range(N) ]
row_sum = [ [0,0,0] for _ in range(N) ]  # W,B,R

result = 10e9

for j in range(M):
    if mat[0][j]=='W':
        row_sum[0][1] += 1
        row_sum[0][2] += 1
    elif mat[0][j]=='B':
        row_sum[0][0] += 1
        row_sum[0][2] += 1
    else :
        row_sum[0][0] += 1
        row_sum[0][1] += 1

for i in range(1,N,1):
    row_sum[i][0], row_sum[i][1], row_sum[i][2] = row_sum[i-1][0], row_sum[i-1][1], row_sum[i-1][2]
    for j in range(M):
        if mat[i][j]=='W':
            row_sum[i][1] += 1
            row_sum[i][2] += 1
        elif mat[i][j]=='B':
            row_sum[i][0] += 1
            row_sum[i][2] += 1
        else :
            row_sum[i][0] += 1
            row_sum[i][1] += 1

for i in range(0,N-2,1):
    for j in range(i+1, N-1, 1):
        result = min(result, row_sum[i][0]+(row_sum[j][1]-row_sum[i][1])+(row_sum[N-1][2]-row_sum[j][2]))

print(result)
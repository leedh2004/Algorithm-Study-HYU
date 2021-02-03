mat = [ [0,0] for _ in range(41) ]
mat[0][0], mat[0][1], mat[1][0], mat[1][1] = 1, 0, 0, 1

for i in range(2, 41, 1):
    mat[i][0] = mat[i-2][0] + mat[i-1][0]
    mat[i][1] = mat[i-2][1] + mat[i-1][1]

T = int(input())
for i in range(T):
    N = int(input())
    print(mat[N][0],mat[N][1])
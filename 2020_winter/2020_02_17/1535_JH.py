import sys
input = sys.stdin.readline

N = int(input())
sad = list(map(int,input().split()))
happy = list(map(int, input().split()))
mat = [ [0 for _ in range(101)] for _ in range(N+1) ]

for i in range(1,N+1):
    for j in range(1, 101, 1):
        now = j-sad[i-1]
        if now > 0 :
            mat[i][j] = max(mat[i-1][now]+happy[i-1], mat[i-1][j])
        else :
            mat[i][j] = mat[i-1][j]

print(mat[N][100])
import sys
input = sys.stdin.readline

N = int(input())
mat = [ list(map(int,input().strip().split())) for _ in range(N) ]
DP1,DP2 = [[0 for _ in range(N+1)] for _ in range(N+1)], [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    DP1[1][i+1], DP1[i+1][1] = mat[0][i], mat[i][0]

for i in range(N):
    DP2[1][i], DP2[i+1][-2] = mat[0][i], mat[i][-1]


for i in range(2,N+1,1):
    for j in range(2,N+1,1):
        DP1[i][j] = DP1[i-1][j-1] + mat[i-1][j-1]

for i in range(2,N+1,1):
    for j in range(0,N-1,1):
        DP2[i][j] = DP2[i-1][j+1] + mat[i-1][j]

for _ in range(N+1):
    print(DP1[_])

print('-----------------------')

for _ in range(N+1):
    print(DP2[_])

result = 0


for i in range(N):
    for j in range(N):
        gap_rng = min(N-i, N-j)
        for gap in range(1, gap_rng, 1):
            result = max(result, (DP1[i+gap+1][j+gap+1]-DP1[i][j]) - (DP2[i+1+gap][j]-DP2[i][j+gap+1]) )

print(result)
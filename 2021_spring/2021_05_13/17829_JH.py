import sys
input = sys.stdin.readline

N = int(input().strip())
mat = [ list(map(int,input().strip().split())) for _ in range(N) ]

def solution(N, mat):
    if N == 1 :
        print(mat[0][0])
        exit()
    nn = N//2
    next_mat = [ [] for i in range(nn) ]

    for i in range(0, N, 2) :
        for j in range(0, N, 2) :
            tmp = [ mat[i][j], mat[i][j+1], mat[i+1][j], mat[i+1][j+1] ]
            tmp.sort()
            next_mat[i//2].append(tmp[-2]) 

    solution(nn, next_mat)

solution(N,mat)
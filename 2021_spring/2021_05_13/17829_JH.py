import sys
input = sys.stdin.readline

N = int(input().strip())
mat = [ list(map(int,input().strip().split())) for _ in range(N) ]

def solution(N, mat):
    if N == 1 :
        return mat[0][0]
    nn = N//2
    next_mat = [ [] for i in range(nn) ]

    for i in range(0, N, 2) :
        for j in range(0, N, 2) :
            tmp = [ mat[i][j], mat[i][j+1], mat[i+1][j], mat[i+1][j+1] ]
            tmp.sort()
            next_mat[i//2].append(tmp[-2]) 
    return solution(nn, next_mat)

print(solution(N,mat))
import sys


def row_check(A, N, L):

    check = [True] * N

    for i in range(N):
        line = A[i]
        slope = [False]*N
        for j in range(N-1):
            if(line[j] == line[j+1]):
                continue
            if(abs(line[j+1]-line[j]) > 1):
                check[i] = False
                break
            elif(line[j] + 1 == line[j+1] and j+1-L >= 0):
                tmp = line[j]
                for k in range(j, j-L, -1):
                    if(line[k] != tmp):
                        check[i] = False
                        break
                for k in range(j, j-L, -1):
                    if(slope[k]):
                        check[i] = False
                        break
                for k in range(j, j-L, -1):
                    slope[k] = True
                continue
            elif(line[j] - 1 == line[j+1] and j+L <= N-1):
                tmp = line[j+1]
                for k in range(j+1, j+L+1):
                    if(line[k] != tmp):
                        check[i] = False
                        break
                for k in range(j+1, j+L+1):
                    slope[k] = True
                j = j+L-1
                continue
            else:
                check[i] = False
    cnt = 0
    for i in range(N):
        if(check[i] == True):
            cnt += 1

    return cnt


def col_check(A, N, L):
    B = [[0]*N for _ in range(N)]
    check = [True] * N
    for i in range(N):
        for j in range(N):
            B[i][j] = A[j][i]

    for i in range(N):
        line = B[i]
        slope = [False]*N
        for j in range(N-1):
            if(line[j] == line[j+1]):
                continue
            if(abs(line[j+1]-line[j]) > 1):
                check[i] = False
                break
            elif(line[j] + 1 == line[j+1] and j+1-L >= 0):
                tmp = line[j]
                for k in range(j, j-L, -1):
                    if(line[k] != tmp):
                        check[i] = False
                        break
                for k in range(j, j-L, -1):
                    if(slope[k]):
                        check[i] = False
                        break
                for k in range(j, j-L, -1):
                    slope[k] = True
                continue
            elif(line[j] - 1 == line[j+1] and j+L <= N-1):
                tmp = line[j+1]
                for k in range(j+1, j+L+1):
                    if(line[k] != tmp):
                        check[i] = False
                        break
                for k in range(j+1, j+L+1):
                    slope[k] = True
                j = j+L-1
                continue
            else:
                check[i] = False

    cnt = 0
    for i in range(N):
        if(check[i] == True):
            cnt += 1
    return cnt


N, L = map(int, sys.stdin.readline().split())

A = [[0]*N for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, sys.stdin.readline().split()))

print(row_check(A, N, L)+col_check(A, N, L))

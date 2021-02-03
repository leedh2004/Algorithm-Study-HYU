# 1. 방향 그래프를 만듦
# 2. a애서 b로 가는 길이 없고 b에서 a로 가는 길도 없다면 a와 b를 비교할 수 없다.

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 10e20
mat = [[INF for _ in range(N)] for i in range(N)]

for i in range(M):
    s,e = map(int,input().split())
    mat[s-1][e-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

for i in range(N):
    result = 0
    for j in range(N):
        if i == j :
            continue
        if mat[i][j] == INF and mat[j][i] == INF :
            result += 1
    print(result)
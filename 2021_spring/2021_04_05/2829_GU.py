import sys


def find_diagmax(sz):
    ans = -(sys.maxsize)
    for i in range(sz-1, N):
        for j in range(N-sz+1):
            # print("i,j", i, j)
            ans = max(ans, A_sum[i][j+sz-1] - B_sum[i][j])
            if ans != -1:
                print(ans, i, j)
    return ans


N = int(sys.stdin.readline())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))
# 대각선 누적합
A_sum = [[0 for _ in range(N)] for _ in range(N)]
B_sum = [[0 for _ in range(N)] for _ in range(N)]

# 가장 긴 대각선
A_sum[0][0] = matrix[0][0]
for i in range(1, N):
    A_sum[i][i] = A_sum[i-1][i-1] + matrix[i][i]

B_sum[0][N-1] = matrix[0][N-1]
j = N-2
for i in range(1, N):
    B_sum[i][j] = B_sum[i-1][j+1] + matrix[i][j]
    j -= 1

# 나머지 대각선
# i - 왼쪽줄 시작 idx / j = y축 idx / k = x축 idx
for i in range(1, N-1):
    A_sum[i][0] = matrix[i][0]
    k = 1
    for j in range(i+1, N):
        A_sum[j][k] = A_sum[j-1][k-1] + matrix[j][k]
        k += 1

for i in range(1, N-1):
    A_sum[0][i] = matrix[0][i]
    k = 1
    for j in range(i+1, N):
        A_sum[k][j] = A_sum[k-1][j-1] + matrix[k][j]
        k += 1

for i in range(N-2, 0, -1):
    B_sum[0][i] = matrix[0][i]
    k = 1
    for j in range(i-1, -1, -1):
        B_sum[k][j] = B_sum[k-1][j+1] + matrix[k][j]
        k += 1

for i in range(1, N-1):
    B_sum[i][N-1] = matrix[i][N-1]
    k = N-2
    for j in range(i+1, N):
        B_sum[j][k] = B_sum[j-1][k+1] + matrix[j][k]
        k -= 1

print(A_sum)
print(B_sum)
print(find_diagmax(2))

import sys

d = [[0 for _ in range(10)] for _ in range(65)]

for i in range(10):
    d[1][i] = 1

for i in range(2,65):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][j]
        else:
            for k in range(j+1):
                d[i][j] += d[i-1][k]

T = int(sys.stdin.readline())
for i in range(T):
    print(sum(d[int(sys.stdin.readline())]))
import sys
INF = sys.maxsize

n, m = map(int,sys.stdin.readline().split())
d = []
for i in range(n):
    tmp = [INF for _ in range(n)]
    tmp[i] = 0
    d.append(tmp)
for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    d[a-1][b-1] = 1
    #d[b-1][a-1] = -1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k]+d[k][j]
check = [0] * n
for i in range(n):
    for j in range(n):
        if d[i][j] != INF and d[i][j] > 0:
            check[i] += 1
            check[j] += 1
print(check.count(n-1))
"""#dontKnow = False
for i in range(n):
    student = d[i]
    for j in range(n):
        if student[j] != INF:
            continue
        else:
            tmp = d[j]
            if tmp[i] == INF:
                dontKnow = True
                break
    if not dontKnow:
        cnt += 1
    else:
        dontKnow = False
print(cnt)"""

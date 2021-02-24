import sys


def find(x):
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


N, M = map(int, sys.stdin.readline().split())
parent = [x for x in range(N+1)]
gender = list(sys.stdin.readline().rstrip().split())
ways = []
for _ in range(M):
    u, v, d = list(map(int, sys.stdin.readline().split()))
    if gender[u-1] != gender[v-1]:
        ways.append([d, u, v])
ways.sort()

ans = 0
cnt = 0
for i in range(len(ways)):
    d, u, v = ways[i]
    if find(u) == find(v):
        continue
    ans += d
    cnt += 1
    union(u, v)

if cnt == N-1:
    print(ans)
else:
    print(-1)

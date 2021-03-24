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


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [x for x in range(N+1)]

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if tmp[j] == 1:
            union(i+1, j+1)

dest = list(map(int, sys.stdin.readline().split()))
p = find(dest[0])
possible = True
for i in range(1, len(dest)):
    if find(dest[i]) != p:
        possible = False
        break
if possible:
    print("YES")
else:
    print("NO")

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
mat = [ list(map(int,input().strip().split())) for _ in range(N) ]
uni = {i:i for i in range(N)}

def find(x):
    global uni
    if uni[x] != x :
        uni[x] = find(uni[x])
        return uni[x]
    else :
        return x

def union(x,y):
    global uni
    a,b = find(x), find(y)
    if a != b :
        uni[b] = a


for i in range(N):
    for j in range(N):
        if mat[i][j] == 1  :
            union(i,j)

L = list(map(lambda x : int(x)-1,input().strip().split()))

for i in range(0,M-1,1):
    if find(L[i]) != find(L[i+1]):
        print('NO')
        exit()

print('YES')

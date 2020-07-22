import sys

def find(x):
    global parent
    if parent[x] == x: return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y
def union(x,y):
    x = find(x)
    y = find(y)
    if x!= y:
        parent[y] = x

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = list(range(n+1))
#parent = parent[1:]
ways = []
for i in range(m):
    ways.append(list(map(int,sys.stdin.readline().split())))
ways.sort(key = lambda x:x[2])
res = 0
cnt = 0
for i in range(m):
    a,b,c = ways[i]
    if cnt == n-1: break
    elif a == b:
        continue 
    if find(a) != find(b):
        union(a,b)
        res += c
        cnt += 1
print(res)
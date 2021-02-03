import sys  

def find(x):
    if parent[x] == x: return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y: parent[y] = x

N,M = map(int,sys.stdin.readline().split())
#Union-Find
parent = [x for x in range(N+1)]
ways = []
for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    ways.append([c,a,b])
#Kruskal
ways.sort()
res = 0
cnt = 0
for i in range(M):
    c,a,b = ways[i]
    if find(a) == find(b): continue
    else:
        res += c
        cnt += 1
        union(a,b)
        #Kruskal 쓴 다음 마지막으로 이은 간선 제거
        # -> 최소의 길 가진 두 마을 
        if cnt == N-1:
            res -=c
            break
print(res)

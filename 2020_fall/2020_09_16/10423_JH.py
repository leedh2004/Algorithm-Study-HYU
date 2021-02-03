def find(x) :
    global uni
    if uni[x] == -1 :
        return -1
    if uni[x] == x :
        return x
    else :
        y = find(uni[x])
        uni[x] = y
        return y

def union(x,y):
    global uni
    tmp_x, tmp_y = find(x), find(y)
    if tmp_x != tmp_y :
        if tmp_y == -1 :
            uni[tmp_x] = tmp_y
        else :
            uni[tmp_y] = tmp_x

def kruskal():
    global uni, adj, result
    for c,s,d in adj :
        if s != d and find(s) != find(d) :
            union(s,d)
            result += c
    
    print(result)

N,M,K = map(int,input().split())
ps = list(map(int,input().split()))
uni = [ _ for _ in range(N)]
for i in ps:
    uni[i-1] = -1
adj = []
result = 0
for i in range(M):
    s,d,c = map(int,input().split())
    adj.append([c,s-1,d-1])
adj.sort()
kruskal()
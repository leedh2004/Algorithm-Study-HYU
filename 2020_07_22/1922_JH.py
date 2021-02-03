#1922 - 네트워크 연결

def find(x):
    global uni
    if(uni[x] == x):
        return x
    else :
        return find(uni[x])

def union(x,y):
    global uni
    tmp_x = find(x)
    tmp_y = find(y)

    if(tmp_x != tmp_y):
        uni[tmp_y] = x

def kruskal():
    global uni, cmat, M
    
    result = 0

    for i in range(M):
        c,s,d = cmat[i]

        if( s!=d and find(s) != find(d) ):
            result += c
            union(s,d)

    print(result)


N = int(input())
M = int(input())
cmat = list()
uni = [0 for _ in range(N)]

for i in range(N):
    uni[i] = i

for i in range(M):
    s,d,c = map(int,input().split())
    cmat.append([c,s-1,d-1])

cmat.sort()

kruskal()
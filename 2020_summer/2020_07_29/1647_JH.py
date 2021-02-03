def find(x):
    global uni
    if(uni[x] == x):
        return x
    else :
        y = find(uni[x])
        uni[x] = y
        return y

def union(a,b):
    global uni
    tmp_a = find(a)
    tmp_b = find(b)

    if(tmp_a!=tmp_b):
        uni[tmp_b] = tmp_a

def kruskal():
    global uni, edge
    global N,M

    result = 0
    maximum = -1
    count = 0
    for i in range(M):
        c,s,d = edge[i]

        if(s!=d and find(s)!=find(d)):
            count += 1
            if(count == N-1):
                break
            # if(c>maximum):
            #     maximum = c 
            result+=c
            union(s,d)
    
    # print(result-maximum)
    print(result)


N, M = map(int,input().split())
uni = [0 for _ in range(N)]
edge = []

for i in range(N):
    uni[i] = i

for i in range(M) : 
    s,d,c = map(int,input().split())
    edge.append([c,s-1,d-1])

edge.sort()
kruskal()
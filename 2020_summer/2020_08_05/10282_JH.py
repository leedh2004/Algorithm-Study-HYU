import heapq
TC = int(input())

while TC :
    n, d, c = map(int,input().split())
    mat = [ [] for _ in range(n) ]

    for i in range(d):
        a,b,s = map(int,input().split())
        mat[b-1].append([a-1,s]) 
    heap = []
    heapq.heappush(heap,[0,c-1])
    dis = [100000000001 for _ in range(n)]
    dis[c-1] = 0

    while heap :
        cost, node = heapq.heappop(heap)
        for t, w in mat[node]:
            wei = cost+w
            if dis[t] > wei:
                dis[t] = wei
                heapq.heappush(heap,[wei,t])

    count = 0
    time = 0
    for i in dis :
        if i != 100000000001 : 
            count += 1 
            if time < i :
                time = i
    print(count, time)
    TC -= 1
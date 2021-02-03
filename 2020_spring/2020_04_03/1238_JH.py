from heapq import heappush, heappop   #heap에 넣을때 cost,position 순으로 넣어줘야지 반대로하면 position으로 정렬되서 안됨

def dij(a):
    global N
    global INF
    dijm = [INF]*N
    dijm[a-1] = 0
    q = []
    heappush(q,[0,a])
    while q:
        nowc,nowp = heappop(q)
        for p,c in dic[nowp]:
            c += nowc
            if dijm[p-1]>c:
                dijm[p-1] = c
                heappush(q,[c,p])
    return dijm

INF = 1e9
N,M,X = map(int,input().split())
dic = dict()
for i in range(N):
    dic[i+1] = []
result = [0]*N
for i in range(M):
    a,b,c = map(int,input().split())
    # if not(a in dic) :
    #     dic[a] = list()
    dic[a].append([b,c])
# print(dic)

for i in range(N):
    d = dij(i+1)

    if i == X-1:
        for j in range(N):
            result[j] += d[j]
    else :
        result[i] += d[X-1]

# print(result)
print(max(result))





# from heapq import heappush, heappop   

# def dij(a):
#     global INF
#     global N
#     dijm = [INF]*N
#     dijm[a] = 0
#     q = []
#     heappush(q,[0,a])

#     while q :
#         nowc,nowp = heappop(q)
#         for p,c in mat[nowp]:
#             c+=nowc
            
#             if dijm[p]>c:
#                 dijm[p] = c
#                 heappush(q,[c,p])
#     return dijm
    

# INF = 1e9
# N,M,X = map(int,input().split())
# mat = [[] for _ in range(N)]
# result = [0]*N

# for i in range(M):
#     a,b,c = map(int,input().split())
#     mat[a-1].append([b-1,c])

# for i in range(N):
#     d = dij(i)
#     if i == X-1 :
#         for j in range(N):
#             result[j] += d[j]
#     else :
#         result[i] += d[X-1]

# print(max(result))
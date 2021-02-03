N = int(input())
L = list()
count = 1
idx = 0
for i in range(N):
    s, e = map(int, input().split())
    L.append((s,e))

L = sorted(L, key = lambda x : x[0])
L = sorted(L, key = lambda x : x[1])

for i in range(1,len(L)) :
    if L[i][0] >= L[idx][1] :
        count+=1
        idx = i

print(count)
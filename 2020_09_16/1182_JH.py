N, S = map(int,input().split())
L = list(map(int,input().split()))
tmp = list()
result = 0
for i in range(len(L)):
    tmp.append(L[i])
    if (L[i] == S) :
        result += 1
    for j in range(len(tmp)-2,-1,-1):
        if (tmp[j]+L[i]) == S :
            result += 1
        tmp.append(tmp[j]+L[i])
print(result)
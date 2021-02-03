N = int(input())
L = list(map(int,input().split()))
result = [1 for _ in range(N)]

for i in range(len(L)):
    for j in range(i-1,-1,-1):
        if L[j] > L[i] :
            result[i] = max(result[i], result[j]+1)

print(max(result))
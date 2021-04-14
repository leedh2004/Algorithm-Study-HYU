import sys
input = sys.stdin.readline

N = int(input().strip())
L = list(map(lambda x : bool(int(x)), input().strip().split()))
result = 0

for i in range(N):
    if L[i] :
        result += 1
        for j in range(i+1,i+3,1):
            if j == N :
                break
            L[j] = not L[j]

print(result)
import sys
input = sys.stdin.readline

T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    L = list(map(int,input().strip().split()))
    L.sort()
    result = -1
    for i in range(2,N):
        result = max(result, abs(L[i]-L[i-2]))
    print(result)

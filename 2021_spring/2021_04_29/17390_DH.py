import sys 
N, Q = map(int, sys.stdin.readline().strip().split())
L = list(map(int, sys.stdin.readline().strip().split()))
L = L + [0]
L.sort()
for i in range(1, len(L)):
    L[i] = L[i-1] + L[i]
for _ in range(Q):
    l, r = map(int, sys.stdin.readline().strip().split())
    print(L[r] - L[l-1])
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    L = sorted(list(map(int, sys.stdin.readline().split())))
    #L = deque(sorted(list(map(int, sys.stdin.readline().split()))))
    max_nan = L[1]-L[0]
    left, right = L[0], L[1]
    for i in range(2, N):
        if L[i]-left >= L[i]-right:
            max_nan = max(max_nan, L[i]-left)
            left = L[i]
        else:
            max_nan = max(max_nan, L[i]-right)
            right = L[i]
    print(max_nan)

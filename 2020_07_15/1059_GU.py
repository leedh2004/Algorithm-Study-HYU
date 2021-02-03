import sys

L = int(sys.stdin.readline())
Ls = list(map(int,sys.stdin.readline().split()))
N = int(sys.stdin.readline())
if N in Ls:
    print(0)
else:
    Ls.append(N)
    Ls.sort()
    idx = Ls.index(N)
    if idx == 0:
        right = Ls[idx+1]
        print((right-N-1) + (N-1) + (right-N-1) * (N-1))
    else:
        left = Ls[idx-1]
        right = Ls[idx+1]
        print((N - left -1) + (right - N - 1) + (N - left -1) * (right - N - 1))


    
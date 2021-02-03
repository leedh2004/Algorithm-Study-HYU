import sys

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    d = [0, 1, 1, 1, 2, 2]
    if N <= 5: print(d[N])
    else:
        for j in range(N-5):
            P = d[j+1] + d[j+5]
            d.append(P)
        print(d[N])
            
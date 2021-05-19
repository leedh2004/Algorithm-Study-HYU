import sys
import math

N = int(sys.stdin.readline().strip())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

M = 0
A = [0]
B = [0]

for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    A.append(a)
    B.append(b)
    if a < 0:
        M = gcd(b - B[i] - a, M)

s = 0
for i in range(1, N+1):
    if B[i] - B[i-1] == A[i]:
        continue
    
    if M and M <= B[i] or A[i] > 0 or A[i] < 0 and -A[i] < B[i-1]:
        print(-1)
        sys.exit(0)

    if A[i] >= 0:
        s = s + A[i]
        if s != B[i]:
            print(-1)
            sys.exit(0)
    else:
        if B[i] >= M and M or -A[i] < B[i-1]:
            print(-1)
            sys.exit(0)
        s = B[i]

print(1 if M == 0 else M)


import sys

def find(a,b):
    while b!=0:
        n = a%b
        a = b
        b = n
    return a

T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    gcd = 0
    if A > B: gcd = find(A,B)
    else: gcd = find(B,A)
    print((A//gcd)*(B//gcd)*gcd)
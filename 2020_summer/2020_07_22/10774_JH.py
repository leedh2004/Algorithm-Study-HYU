#10774 - 저지

J = int(input())
A = int(input())
U = [ 0 for _ in range(1000000) ]
result = 0

for i in range(J):
    U[i] = ord(input())

for i in range(A):
    s,n = input().split()
    s = ord(s)
    n = int(n)
    if(U[n-1] != 0 and U[n-1] <= s):
        U[n-1] = 1000001
        result += 1

print(result)
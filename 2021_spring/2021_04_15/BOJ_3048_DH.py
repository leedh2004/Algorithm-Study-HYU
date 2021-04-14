_, __ = input().split()
A = input()
B = input()
T = int(input())
A = A[::-1] # reverse 
C = A + B
C = list(C)
for _ in range(T):
    i = 0
    while i < len(C) - 1:
        if C[i] in A and C[i+1] in B:
            C[i], C[i+1] = C[i+1], C[i]
            i += 1
        i+= 1
print("".join(C))
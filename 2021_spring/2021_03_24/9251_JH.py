import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

L_A, L_B = len(A), len(B)

DP = [ [0 for _ in range(L_A+1)] for i in range(L_B+1) ]

for j in range(L_B):
    for i in range(L_A):
        if B[j] == A[i] :
            DP[j+1][i+1] = max(DP[j][:i+1]) + 1
        else :
            DP[j+1][i+1] = DP[j][i+1]

print(max(DP[L_B]))
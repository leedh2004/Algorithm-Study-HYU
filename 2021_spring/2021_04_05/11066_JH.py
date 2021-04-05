import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input().strip())
    L = list(map(int,input().strip().split()))
    
    DP = [ [0 for i in range(K)] for j in range(K) ]
    psum = [0 for i in range(K)]
    psum[0] = L[0]

    for i in range(1,K):
        psum[i] = psum[i-1]+L[i]

    for i in range(0, K-1, 1):
        DP[i][i+1] = psum[i+1] - psum[i]

    for i in range(K-2, -1, -1):
        for j in range(i+1, K, 1)
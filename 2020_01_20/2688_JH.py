import sys
input = sys.stdin.readline

DP = [[0 for _ in range(10)] for i in range(65) ]
DP[1] = [1 for _ in range(10)]


def solution(n):
    global DP
    if DP[n][0] != 0 :
        return
    if DP[n-1][0] == 0 :
        solution(n)
    
    DP[n][0] = 1
    for i in range(1,10):
        for j in range(i,-1,-1):
            DP[n][i] += DP[n-1][j]

T = int(input())
for a in range(T):
    n = int(input())
    solution(n)
    print(sum(DP[n]))
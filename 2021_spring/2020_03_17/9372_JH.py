import sys
input = sys.stdin.readline

C = int(input())

for i in range(C):
    N,M = map(int,input().split())
    for j in range(M):
        s,e, = map(int,input().split())
    print(N-1)
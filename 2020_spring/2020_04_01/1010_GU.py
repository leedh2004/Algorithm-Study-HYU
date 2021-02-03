import sys
import itertools


T = int(sys.stdin.readline())

for i in range(T):
    bottom = 1
    upper =1
    N,M = map(int,sys.stdin.readline().split())
    for j in range(1,N+1):
        bottom *= j
    for j in range(M,M-N,-1):
        upper *= j
    print(upper//bottom)    
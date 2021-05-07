import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
d = sorted(data)

idxF,idxR = 0, n-1
ansF,ansR = 0, n-1
mind = 2000000001

while idxF<idxR:
    nowd = d[idxF] + d[idxR]
    posnowd = abs(d[idxF] + d[idxR])

    if posnowd < mind:
        mind = posnowd
        ansF,ansR = idxF,idxR

    if nowd < 0:
        idxF = idxF + 1
    else :
        idxR = idxR - 1

print(d[ansF],d[ansR])





import sys

d = [-1 for _ in range(1001)]
d[1], d[2], d[3], d[4], d[5] = 1, 0, 1, 1, 1
for i in range(6, 1001):
    if d[i-1]+d[i-3]+d[i-4] < 3:
        d[i] = 1
    else:
        d[i] = 0

N = int(sys.stdin.readline())
if d[N]:
    print("SK")
else:
    print("CY")

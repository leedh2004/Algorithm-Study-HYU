import sys

N = int(sys.stdin.readline())
if(N<1 or N > 1000000):
    sys.exit(1)
d = [-1 for _ in range(N+1)]

d[0] = 0
d[1] = 0
if(N>1):
    d[2] = 1
if(N>2):
    d[3] = 1
a = []
for i in range(4,N+1):
    if(i%3 == 0):
        a.append(d[int(i/3)])
    if(i%2 == 0):
        a.append(d[int(i/2)])
    a.append(d[i-1])
    d[i] = min(a)+1
    a.clear()
print(d[N])

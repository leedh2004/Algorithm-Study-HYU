import sys

N = int(sys.stdin.readline())
if(N<1 or N>10000):
    sys.exit(1)
d = [0]
w = [0]
for i in range(N):
    w.append(int(sys.stdin.readline()))
d.append(w[1])
if N>1:
    d.append(w[1]+w[2])
for i in range(3,N+1):
    d.append(max(d[i-1],d[i-2]+w[i],d[i-3]+w[i-1]+w[i]))

print(d[N])

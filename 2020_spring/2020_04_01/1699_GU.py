import sys
import math

N = int(sys.stdin.readline())
d = [0 for _ in range(N+1)]
sq_max = int(math.sqrt(N))

for i in range(1,N+1):
    i_max = int(math.sqrt(i))
    possible = []
    for j in range(i_max,0,-1):
        possible.append(d[i-int(pow(j,2))])
    d[i] = min(possible) +1
print(d[N])
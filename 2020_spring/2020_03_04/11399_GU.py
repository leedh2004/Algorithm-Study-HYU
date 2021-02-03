import sys
import itertools


N =int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
A = [(i+1,P[i]) for i in range(N)] 
A.sort(key = lambda x:x[1])

time = 0
for i in range(N,0,-1):
    time += A[N-i][1]*i
print(time)


"""#line = list(itertools.permutations([i for i in range(1,N+1)]))

# over the memory sibal


for i in range(len(line)):
    time = 0
    for j in range(N,0,-1):
        time += P[line[i][N-j]-1] * j
    if i==0:
        minimum = time
    if minimum > time:
        minimum = time
print(minimum)
"""
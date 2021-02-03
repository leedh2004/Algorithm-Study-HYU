import sys

def inRange(n):
    return (0<=n) and (n<=M)

#S - start, M - maximum
N,S,M = map(int,sys.stdin.readline().split())
songs = list(map(int,sys.stdin.readline().split()))
d = [[] for _ in range(N+1)]
d[0].append(S)

for i in range(1,N+1):
    cur = d[i-1]
    for j in range(len(cur)):
        if inRange(cur[j] - songs[i-1]):
            d[i].append(cur[j] - songs[i-1])
        if inRange(cur[j] + songs[i-1]):
            d[i].append(cur[j] + songs[i-1])
    #아랫줄 안썼더니 메모리 초과
    d[i] = list(set(d[i]))

if len(d[N]) != 0: print(max(d[N]))
else: print(-1)


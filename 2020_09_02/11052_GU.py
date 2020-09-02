import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))
P.insert(0,0)
#이차원 배열 X, 얕은 복사
d = P[:]
for i in range(2,N+1):
    for j in range(i):
        d[i] = max(d[i],d[i-j]+d[j])
print(d[N])
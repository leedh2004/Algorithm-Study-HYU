import sys

N = int(sys.stdin.readline())

time = [0 for _ in range(N+1)]
price = [0 for _ in range(N+1)]
d = []
for i in range(N):
    time[i],price[i] = map(int,sys.stdin.readline().split())
    d.append(price[i])
d.append(0)

for i in range(N-1,-1,-1):
    if (time[i] + i > N):
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1],price[i] + d[i+time[i]])
print(d[0])

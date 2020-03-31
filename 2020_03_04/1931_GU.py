import sys

N = int(sys.stdin.readline())
tt = []

for i in range(N):
    s,f = map(int,sys.stdin.readline().split())
    tt.append([s,f])
tt.sort(key = lambda x:x[0])
tt.sort(key = lambda x:x[1])

start = tt[0][1]
ans = 1
for i in range(1,N):
    if tt[i][0] >= start:
        ans +=1
        start = tt[i][1]

print(ans)



""" 
dp  time over 

N = int(sys.stdin.readline())
tt = []
early_finish = 2**31-1
for i in range(N):
    s,f = map(int,sys.stdin.readline().split())
    if i ==0:
        last = f
        first = s
    if last < f:
        last = f
    if f < early_finish:
        early_finish = f        
    if first > s:
        first = s
    tt.append([s,f])
sz= last-first +1

d = [0 for _ in range(sz)]
for i in range(early_finish,sz): # loop for d
    for j in range(len(tt)): # loop for tt
        if tt[j][1] == i:
            time = tt[j][1] - tt[j][0]
            d[i] = max(d[i-time]+1,d[i-1])
print(d[sz-1])
"""




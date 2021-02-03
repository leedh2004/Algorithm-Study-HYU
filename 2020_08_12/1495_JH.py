import collections
N, S, M = map(int,input().split())
V = list(map(int,input().split()))
dp = collections.deque()
dp.append(S)
flag = False
for i in range(N):
    check = [False for _ in range(M+1)]
    for j in range(len(dp)):
        t = dp.popleft()
        if(t-V[i]>=0 and check[t-V[i]] == False ):
            dp.append(t-V[i])
            check[t-V[i]] = True
        if(t+V[i]<=M and check[t+V[i]] == False ):
            dp.append(t+V[i])
            check[t+V[i]] = True
    if not dp:
        flag = True
        break

if flag :
    print(-1)
else :
    print(max(dp))
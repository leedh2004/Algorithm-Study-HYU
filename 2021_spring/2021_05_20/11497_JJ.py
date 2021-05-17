import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    l = list(map(int,input().split()))
    l = sorted(l)

    dq = deque([])
    flag = True
    for i in range(n):
        if flag:
            dq.append(l[i])
        else :
            dq.appendleft(l[i])
        flag = not flag
    


    ans = 0
    for i in range(n-1):
        ans = max(ans,abs(dq[i]-dq[i+1]))
    ans = max(ans,abs(dq[0]-dq[n-1]))
    print(ans)

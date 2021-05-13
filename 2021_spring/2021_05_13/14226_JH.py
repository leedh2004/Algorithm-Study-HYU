import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
q = deque()
q.append((1,0))
visit = dict()
visit[(1,0)] = 0

while q :
    s,c = q.popleft()
    if s == N :
        print(visit[(s,c)])
        break

    if (s,s) not in visit.keys():
        visit[(s,s)] = visit[(s,c)]+1
        q.append((s,s))
    if (s+c,c) not in visit.keys():
        visit[(s+c,c)] = visit[(s,c)]+1
        q.append((s+c,c))
    if (s-1,c) not in visit.keys():
        visit[(s-1,c)] = visit[(s,c)]+1
        q.append((s-1,c))
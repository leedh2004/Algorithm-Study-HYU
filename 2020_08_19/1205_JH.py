import sys

N, ns, P = map(int, sys.stdin.readline().split())
score = list(map(int, sys.stdin.readline().split()))
score.append(ns)
score.sort(reverse=True)
nsIndex = score.index(ns)+1

if nsIndex > P or ( ns == score[-1] and N==P ) :
    print(-1)
else :
    print(nsIndex)
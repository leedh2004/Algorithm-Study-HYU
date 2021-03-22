import sys
input = sys.stdin.readline
from collections import deque

N,L = map(int,input().strip().split())
info = deque(sorted([ list(map(int, input().strip().split())) for _ in range(N) ]))
result, last = 0,0


def solution(s,e):
    global L
    length,plus = e-s, 0
    q,r = length // L, length % L
    if r != 0 :
        q += 1
        plus = L-r
    # print(s,e,q,plus)
    return q, plus

while info :
    s,e = info.popleft()
    if s <= last :
        s = last
    q, plus = solution(s,e)
    result += q
    last = e+plus

print(result)
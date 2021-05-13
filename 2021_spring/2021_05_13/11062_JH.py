import sys
input = sys.stdin.readline
from collections import deque

def solution(n, L, left, right):
    if n == 1 :
        return L[0]

    if DP[k] :
        return DP[k]

    DP[k] = max( solution(n-1, L.popleft(), ), solution(n-1, L.pop()) )
    
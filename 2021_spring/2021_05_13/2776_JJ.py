import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    note1 = list(map(int,input().split()))
    nodeHash = defaultdict(bool)
    for key in note1:
        nodeHash[key] = True
    m = int(input())
    note2 = list(map(int,input().split()))
    for key in note2:
        print( 1 if nodeHash[key] else 0)


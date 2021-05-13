import sys
from collections import deque

S = int(sys.stdin.readline())
d = [[-1 for _ in range(S+1)] for _ in range(S+1)]
d[1][0] = 0
# 화면 / 클립보드
q = deque([[1, 0]])

while q:
    sc, clip = q.popleft()
    # 복사
    if d[sc][sc] == -1:
        d[sc][sc] = d[sc][clip] + 1
        q.append([sc, sc])
    # 클립 복붙
    if sc+clip <= S and d[sc+clip][clip] == -1:
        d[sc+clip][clip] = d[sc][clip] + 1
        q.append([sc+clip, clip])
    if sc - 1 >= 0 and d[sc-1][clip] == -1:
        d[sc-1][clip] = d[sc][clip] + 1
        q.append([sc-1, clip])

_min = sys.maxsize
for i in range(S):
    if d[S][i] != -1:
        _min = min(_min, d[S][i])
print(_min)

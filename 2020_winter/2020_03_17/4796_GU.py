import sys

# P일 중, L일동안만 사용할 수 있다. 강산이는 이제 막 V일짜리 휴가를 시작
# 1 < L < P < V
T = 0
while True:
    T += 1
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    ans = 0
    ans = (V // P) * L
    if V % P > L:
        ans += L
    else:
        ans += V % P
    print("Case %d: %d" % (T, ans))

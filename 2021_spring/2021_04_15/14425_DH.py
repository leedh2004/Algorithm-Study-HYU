# 삼성아님
N, M = map(int, input().split())
W = {}
ret = 0
for _ in range(N):
    a = input()
    W[a] = True
for _ in range(M):
    a = input()
    if a in W:
        ret += 1
print(ret)
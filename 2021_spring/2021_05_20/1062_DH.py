from itertools import combinations
N, K = map(int, input().split())
# a, n, t, i, c 는 기본적으로 배워야 함
D = "antic"
B = []
for _ in range(N):
    s = input()
    if K < 5:
        print(0)
        exit(0)
    b = 0 
    for c in s:
        if c in D:
            continue
        diff = ord(c) - ord('a')
        if b & 1 << diff == 0:
            b = b | 1 << diff
    B.append(b)

C = []
for i in range(26):
    c = chr(i + ord('a'))
    if c in D:
        continue
    C.append(c)

ans = 0
for lis in combinations(C, K-5):
    C = 0 
    cand = 0
    for c in lis:
        C = C | 1 << ord(c) - ord('a')
    for b in B:
        if b & C == b:
            cand += 1
    ans = max(ans, cand)
print(ans)

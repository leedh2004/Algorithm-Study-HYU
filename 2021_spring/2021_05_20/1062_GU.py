import sys
import string
from itertools import combinations
# N개 단어, K개 알파벳 배움
# a,c,i,t,n 필수로 알아야함
N, K = map(int, sys.stdin.readline().split())
bitmask = [0 for _ in range(N)]
for i in range(N):
    word = sys.stdin.readline().rstrip()
    for w in word:
        bitmask[i] |= (1 << (ord(w)-ord('a')))

if K < 5:
    print(0)
else:
    lower = list(string.ascii_lowercase)
    lower.remove('a')
    lower.remove('c')
    lower.remove('i')
    lower.remove('t')
    lower.remove('n')
    must_have = ['a', 'c', 'i', 't', 'n']
    comb = list(combinations(lower, K-5))
    ans = 0
    for c in comb:
        each = 0
        res = 0
        # 각 조합에 대한 비트마스킹
        for j in must_have:
            each |= (1 << (ord(j) - ord('a')))
        for j in c:
            each |= (1 << (ord(j) - ord('a')))

        # 단어와 각 조합의 비교
        for j in bitmask:
            if each & j == j:
                res += 1

        # 최대값 갱신
        if ans < res:
            ans = res
    print(ans)

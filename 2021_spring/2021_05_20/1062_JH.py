# 백트래킹이 어디에서 쓰이나요 ??

import sys
input = sys.stdin.readline
from itertools import combinations

N,K = map(int,input().strip().split())
L = list()
alpha = {'b': 0, 'd': 1, 'e': 2, 'f': 3, 'g': 4, 'h': 5, 'j': 6,
            'k': 7, 'l': 8, 'm': 9, 'o': 10, 'p': 11, 'q': 12, 'r': 13,
            's': 14, 'u': 15, 'v': 16, 'w': 17, 'x': 18, 'y': 19, 'z': 20}

def to_bin(w):
    global alpha
    ret = 0b0
    for i in w :
        ret = ret | (1 << alpha[i])
    return ret

for _ in range(N) : 
    L.append( set(input().strip()[4:-4]) - {'a','c','i','t','n'} )

if K < 5 :
    print(0)

else :
    word_to_bin = [ to_bin(w) for w in L ]
    result = 0
    # 1 << o
    powers = [ 2**i for i in range(21) ]

    for case in combinations(powers, K-5):
        now_case = sum(case)
        tmp = 0
        for bw in word_to_bin :
            if now_case & bw == bw :
                tmp += 1
        result = max(result, tmp)

    print(result)
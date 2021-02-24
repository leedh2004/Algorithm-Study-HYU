#26 진수로 표현하는 문제라 생각, 근데 0을 안쓰니까 매번 1칸씩 왼쪽으로 당겨와줘야해서 m = (m//26) -1

import sys
input = sys.stdin.readline

result = []
std = 65
while True:
    RnCm = input().strip()
    C_idx = RnCm.index('C')
    n,m = RnCm[1:C_idx], int(RnCm[C_idx+1:])-1
    C = ''
    if n=='0' and m==-1 :
        break

    while True:
        qu, re = m//26, m%26
        m = (m//26) -1
        if qu == 0 :
            C = chr(std+(re)) + C
            break
        C = chr(std+(re)) + C

    C += n
    print(C)
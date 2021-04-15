import sys
import math

"""
1년마다 5%의 이율을 얻는 투자 (A)
3년마다 20%의 이율을 얻는 투자 (B)
5년마다 35%의 이율을 얻는 투자 (C)
"""


def A(cost):
    return math.floor((1.05)*cost)


def B(cost):
    return math.floor((1.2)*cost)


def C(cost):
    return math.floor((1.35)*cost)


# 초기비용 H 투자기간 Y
H, Y = map(int, sys.stdin.readline().split())
d = [0 for _ in range(Y+1)]
d[0] = H
for i in range(1, Y+1):
    d[i] = A(d[i-1])
    if i >= 3:
        d[i] = max(d[i], B(d[i-3]))
    if i >= 5:
        d[i] = max(d[i], C(d[i-5]))
print(d[Y])

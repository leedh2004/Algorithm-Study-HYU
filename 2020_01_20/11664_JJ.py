import sys

# 거리구하기


def getDistance(a, b):
    tmp = 0
    for i in range(3):
        tmp = tmp + (a[i]-b[i])**2
    return tmp**0.5

# 가운데 구하기


def getPoint(a, b):
    p = []
    for i in range(3):
        p.append((a[i]+b[i])/2)
    return p


val = 10**-6
Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, sys.stdin.readline().split())
A = [Ax, Ay, Az]
B = [Bx, By, Bz]
C = [Cx, Cy, Cz]

while 1:
    P = getPoint(A, B)
    dP = getDistance(P, C)
    dA, dB = getDistance(A, C), getDistance(B, C)
    # print(A, B)
    # print(dA, dP, dB)
    # A쪽
    if dA < dP:
        B = P

    # B쪽
    elif dB < dP:
        A = P

    else:
        if dA < dB:
            B = P
        elif dB < dA:
            A = P
        else:
            break

    if getDistance(A, B) < val:
        break

P = getPoint(A, B)
print(getDistance(P, C))

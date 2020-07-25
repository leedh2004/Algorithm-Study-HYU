import sys
import math

T = int(sys.stdin.readline())
square = []
for i in range(T):
    for j in range(4):
        [x,y] = list(map(int,sys.stdin.readline().split()))
        square.append([x,y])
    sides = []
    for j in range(4):
        side1 = pow((square[j][0]- square[(j+1)%4][0]),2) + pow((square[j][1]-square[(j+1)%4][1]),2)
        side2 = pow((square[j][0]- square[(j+2)%4][0]),2) + pow((square[j][1]-square[(j+2)%4][1]),2)
        side3 = pow((square[j][0]- square[(j+3)%4][0]),2) + pow((square[j][1]-square[(j+3)%4][1]),2)
        sides.append(side1)
        sides.append(side2)
        sides.append(side3)
    sides = list(set(sides))
    if len(sides) == 2 and max(sides) == 2 * min(sides):
        print(1)
    else: print(0)
    sides.clear()
    square.clear()

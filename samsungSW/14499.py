import sys

class pos:
    def __init__(self,x,y):
       self.x = x
       self.y = y

N,M,x,y,K = map(int,sys.stdin.readline().split())
map_num = [[0] * (20) for _ in range(20)]

for i in range(N):
    map_num[i] = list(map(int,sys.stdin.readline().split()))

order = list(map(int,sys.stdin.readline().split()))

dice = [0]*7

cur = pos(x,y)

tmp = 0
for i in range(K):
    if order[i] == 1:
        if not (cur.y+1 <M and 0<= cur.y+1):
            continue
        cur.y += 1
        tmp = dice[3]
        dice[3] = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = tmp
        if map_num[cur.x][cur.y] != 0:
            dice[6] = map_num[cur.x][cur.y]
            map_num[cur.x][cur.y] = 0
        else:
            map_num[cur.x][cur.y] = dice[6]
        print(dice[1])
    elif order[i] == 2:
        if not(cur.y -1 <M and 0 <= cur.y-1):
            continue
        cur.y -= 1
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = tmp
        if map_num[cur.x][cur.y] != 0:
            dice[6] = map_num[cur.x][cur.y]
            map_num[cur.x][cur.y] = 0
        else:
            map_num[cur.x][cur.y] = dice[6]
        print(dice[1])
    elif order[i] == 3:
        if not (cur.x -1 <N and 0 <= cur.x-1):
            continue
        cur.x -= 1
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp
        if map_num[cur.x][cur.y] != 0:
            dice[6] = map_num[cur.x][cur.y]
            map_num[cur.x][cur.y] = 0
        else:
            map_num[cur.x][cur.y] = dice[6]
        print(dice[1])
    elif order[i] == 4:
        if not (cur.x +1 < N and 0 <= cur.x+1):
            continue
        cur.x += 1
        tmp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = tmp
        if map_num[cur.x][cur.y] != 0:
            dice[6] = map_num[cur.x][cur.y]
            map_num[cur.x][cur.y] = 0
        else:
            map_num[cur.x][cur.y] = dice[6]
        print(dice[1])

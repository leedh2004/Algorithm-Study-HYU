R, C, T = map(int, input().split())
B = []
for _ in range(R):
    t = list(map(int, input().split()))
    B.append(t)
def printb():
    for i in range(R):
        for j in range(C):
            print(B[i][j], end=' ')
        print()
# 진공청소기의 위치 
sy = 0
for i in range(R):
    if B[i][0] == -1 and B[i+1][0] == -1:
        sy = i
        break

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
D2 = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in range(T):
    # 확산
    new_B = [ [0 for _ in range(C)] for _ in range(R) ]
    new_B[sy][0], new_B[sy+1][0] = -1, -1
    for y in range(R):
        for x in range(C):
            if B[y][x] > 0:
                cnt = 0
                val = B[y][x]
                for dy, dx in D:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < R and 0 <= nx < C and B[ny][nx] != -1:
                        new_B[ny][nx] += val // 5
                        cnt += 1
                new_B[y][x] += val - ((val // 5) * cnt)
            
    B = new_B
    y, x, cnt = sy - 1, 0, 0
    while not (y == sy and x == 1):
        ny, nx = y + D[cnt][0], x + D[cnt][1]
        if 0 <= ny < sy + 1 and 0 <= nx < C:
            if B[y][x] != -1:
                B[y][x] = B[ny][nx]
            y, x = ny, nx
        else:
            cnt += 1
            continue
    y, x, cnt = sy + 2, 0, 0
    while not (y == sy + 1 and x == 1):
        ny, nx = y + D2[cnt][0], x + D2[cnt][1]
        if sy + 1 <= ny < R and 0 <= nx < C:
            if B[y][x] != -1:
                B[y][x] = B[ny][nx]
            y, x = ny, nx
        else:
            cnt += 1
            continue
    B[sy][1], B[sy+1][1] = 0, 0

print(sum([ sum(B[i]) for i in range(R) ]) + 2)




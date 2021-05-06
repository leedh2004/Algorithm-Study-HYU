# 2: 17
import sys

N = int(sys.stdin.readline().strip())
B = []

for _ in range(N):
    t = list(map(int, sys.stdin.readline().strip().split()))
    B.append(t)

# 왼쪽, 아래, 오른쪽, 위쪽이동
# 한 번 돌때마다 2씩 증가 시켜줘야 함.
M = [(0, -1, 1), (1, 0, 1), (0, 1, 2), (-1, 0, 2)]
def update_M(M):
    M = [(y, x, cnt+2) for y, x, cnt in M]
    # print(M)
    return M

SPECIAL_CASE = -1
# 왼쪽 (0, -1)인 경우
# 총 10개로 나누어짐
def make_D(move):
    D = [
        (0, -2, 0.05), 
        (1, -1, 0.1), (-1, -1, 0.1),
        (1, 0, 0.07), (2, 0, 0.02), (-1, 0, 0.07), (-2, 0, 0.02),
        (1, 1, 0.01), (-1, 1, 0.01), (0, -1, SPECIAL_CASE)
    ]
    if move == 0: # LEFT
        return D 
    elif move == 1: # DOWN
        D = [ (-x, y, p) for y, x, p in D]
        return D
    elif move == 2: # RIGHT
        D = [ (y, -x, p) for y, x, p in D]
    elif move == 3: # UP
        D = [ (x, y, p) for y, x, p in D]
    return D 
    
y, x = N // 2, N // 2
ret = 0 

def printb():
    global B
    print("===========")
    for i in range(N):
        for j in range(N):
            print(B[i][j], end=' ')
        print()
    print("===========")

print(y, x)
ans = 0

while True:
    for (idx, (dy, dx, cnt)) in enumerate(M):
        k = 0 
        while k < cnt:
            y, x = y + dy, x + dx
            if B[y][x] > 0:
                ret = 0
                D = make_D(idx)
                for ddy, ddx, p in D:
                    ny, nx = y + ddy, x + ddx
                    if p != SPECIAL_CASE: ret += int(B[y][x] * p)
                    if 0 <= ny < N and 0 <= nx < N:
                        if p == SPECIAL_CASE:
                            B[ny][nx] = B[y][x] - ret
                        else:
                            B[ny][nx] += int(B[y][x] * p)
                    else:
                        if p != SPECIAL_CASE: ans += int(B[y][x] * p)
                        else: ans += B[y][x] - ret
                B[y][x] = 0
                printb()
            k += 1
            if y == 0 and x == 0:
                print(y, x)
                print(ret)
                printb()
                print(sum([sum(b) for b in B]))
                print(ans)
                exit()
        print(y, x)
    M = update_M(M)
    

print(ret)


N = int(input())
board = [ [0] * 101 for _ in range(101) ]

D = [ (0, 1), (-1, 0), (0, -1), (1, 0) ]

def move(y, x, directions):
    global board, D
    for direction in directions:
        direction = int(direction)
        y = y + D[direction][0]
        x = x + D[direction][1]
        board[y][x] = 1

for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[y][x] = 1
    d = str(d)
    for _ in range(g):
        n = ""
        r = reversed(d)
        for direction in r:
            direction = str((int(direction) + 1) % 4)
            n += direction
        d = d + n
    move(y, x, d)
ans = 0

for y in range(101 - 1):
    for x in range(101 - 1):
        if board[y][x] == 1 and board[y+1][x] == 1 and board[y][x+1] == 1 and board[y+1][x+1] == 1:
            ans += 1
print(ans)


    # R -> U, U -> L, L -> D, D -> R
    # 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0
    # R | U
    # RU | LU
    # RULU | LDLU
    # RULULDLU | LD
    
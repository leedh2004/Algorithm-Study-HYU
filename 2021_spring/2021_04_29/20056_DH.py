import sys 
import pprint

N, M, K = map(int, sys.stdin.readline().strip().split()) 

board = [[0] * (N+1) for _ in range(N+1)]
D = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().strip().split())
    board[r][c] = [(m, s, d)]

def move():
    global board, N
    moved = [[0] * (N+1) for _ in range(N+1)]
    for y in range(1, N+1):
        for x in range(1, N+1):
            if board[y][x] == 0:
                continue
            for m, s, d in board[y][x]:
                ny, nx = y + D[d][0] * s, x + D[d][1] * s
                if ny > N: # N + 1 => 1, N + N + 1 =>1
                    ny = ny % N
                if nx > N:
                    nx = nx % N
                if ny <= 0: # 0 -> N, -1 -> N - 1, -N => N
                    ny = N - abs(ny) % N 
                if nx <= 0:
                    nx = N - abs(nx) % N
                if moved[ny][nx] == 0:
                    moved[ny][nx] = [(m, s, d)]
                else:
                    moved[ny][nx].append((m, s, d))
    # 합친 후 분열
    for y in range(1, N+1):
        for x in range(1, N+1):
            if moved[y][x] == 0:
                continue
            else:
                sum_s, sum_m, odd_cnt, even_cnt = 0, 0, 0, 0
                if len(moved[y][x]) == 1:
                    continue
                for m, s, d in moved[y][x]:
                    sum_s += s
                    sum_m += m
                    if d % 2 == 0: even_cnt += 1
                    else: odd_cnt += 1
                new_m = int(sum_m / 5.0)

                if new_m == 0:
                    moved[y][x] = 0
                    continue
                
                new_s = int(sum_s/ (odd_cnt + even_cnt))
                if odd_cnt == 0 or even_cnt == 0:
                    moved[y][x] = [ (new_m, new_s, i*2 )for i in range(4) ]
                else:
                    moved[y][x] = [ (new_m, new_s, i*2+1 )for i in range(4) ]
    board = moved

for _ in range(K):
    move()
ret = 0
for y in range(1, N+1):
    for x in range(1, N+1):
        if board[y][x] != 0:
            for m, s, d in board[y][x]:
                ret += m
print(ret)
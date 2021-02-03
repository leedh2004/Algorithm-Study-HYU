import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
board[0][0]=1

r = 0
c = 0
for i in range(K):
    r,c = map(int,sys.stdin.readline().split())
    if r>= 1 and c >=1:
        board[r-1][c-1] = 2
    

L = int(sys.stdin.readline())

secs= [0 for _ in range(L+1)]
direction=[0 for _ in range(L+1)]

for i in range(L):
    s,dr = sys.stdin.readline().split()
    secs[i] = int(s)
    direction[i] = dr

dx = [0,1,0,-1]
dy = [-1,0,1,0]

sec = 0
x = 0
y = 0
ht = 0 # head turn
tt = 0 # tail turn
d = 1
tail_d = 1
tail = [0,0]
while(True):
    sec +=1
    next_x = x+ dx[d]
    next_y = y + dy[d]
    
    if next_x < 0 or next_x >=N or next_y < 0 or next_y >=N:
        break
    if board[next_y][next_x] == 1:
        break
    
    x = next_x
    y = next_y

    if board[y][x] == 2:
        board[tail[0]][tail[1]] = 1
        board[y][x] = 1
    elif board[y][x] == 0:
        board[y][x] = 1
        board[tail[0]][tail[1]] = 0
        next_t_y = tail[0] + dy[tail_d]
        next_t_x = tail[1] + dx[tail_d]

        if (next_t_x < 0 or next_t_x >=N or next_t_y < 0 or next_t_y >=N):
            if tt < L:
                if direction[tt] == 'L':
                    tail_d = (tail_d+3)%4
                elif direction[tt] == 'D':
                    tail_d = (tail_d+1)%4
                tt += 1
            else:
                break
        tail[0] = tail[0] + dy[tail_d]
        if(tail[0] < 0 or tail[0] >=N):
            break
        tail[1] = tail[1] + dx[tail_d]
        if(tail[1] < 0 or tail[1] >=N):
            break
        board[tail[0]][tail[1]] = 1

    if ht < L:
        if sec == secs[ht]:
            if direction[ht] == 'L':
                d = (d+3)%4
            elif direction[ht] == 'D':
                d = (d+1)%4
            ht += 1

print(sec)        



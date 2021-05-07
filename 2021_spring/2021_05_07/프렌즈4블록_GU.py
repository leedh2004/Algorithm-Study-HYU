def inRange(m, n, y, x):
    return ((0 <= y < m) and (0 <= x < n))


def gonna_pop(board, m, n, y, x):
    t = board[y][x]
    if t == '0':
        return False
    dy, dx = [0, 0, 1, 1], [0, 1, 0, 1]
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if not inRange(m, n, ny, nx):
            return False
        else:
            if board[ny][nx] != t:
                return False
    return True


def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    before = 0
    while True:
        this_turn = 0
        P = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if gonna_pop(board, m, n, i, j):
                    P[i][j] = True
                    P[i][j+1] = True
                    P[i+1][j] = True
                    P[i+1][j+1] = True
        vertical = ['' for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if P[i][j]:
                    board[i][j] = '0'
                    answer += 1
                    this_turn += 1
                vertical[j] += board[i][j]

        # pop
        for i in range(n):
            vertical[i] = vertical[i].replace('0', '')
            vertical[i] = vertical[i].zfill(m)
            vertical[i] = list(vertical[i])
            for j in range(m):
                board[j][i] = vertical[i][j]

        if this_turn == 0:
            break

    return answer

from copy import deepcopy

def solution(m, n, board):
    answer = 0
    board = [list(board[_]) for _ in range(m)]
    d = [ [0,0], [1,0], [0,1], [1,1] ]

    while True :
        flag = True
        new_board = deepcopy(board)

        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]!='*' and board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]:
                    for dx,dy in d :
                        nx,ny = i+dx, j+dy
                        if new_board[nx][ny] != '*':
                            new_board[nx][ny] = '*'
                            answer += 1
                            flag = False

        if flag :
            break

        for j in range(n):
            new_col = ""
            for i in range(m):
                if new_board[i][j]!='*':
                    new_col+=new_board[i][j]
            new_col = '*'*(m-len(new_col)) + new_col

            for i in range(m):
                new_board[i][j] = new_col[i]

        board = new_board

    return answer


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
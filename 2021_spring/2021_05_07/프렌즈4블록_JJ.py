def solution(m, n, board):
    answer = 0
    newboard = rotate90(m,n,board)
    # print(newboard)
    flag = False
    
    while 1:
        printTable(newboard)
        print('')
        flag = False 
        
        check = [ [True for _ in range(m)] for _ in range(n)]
        for r in range(n-1):
            for c in range(m-1):
                if newboard[r][c] != '*' and newboard[r][c] == newboard[r+1][c] == newboard[r][c+1] == newboard[r+1][c+1]:
                    check[r][c] = check[r+1][c] = check[r][c+1] = check[r+1][c+1] = False
                    flag = True
        
        for r in range(n):
            newc = ['*' for _ in range(m)]
            idx = 0
            for c in range(m):
                if check[r][c]:
                    newc[idx] = newboard[r][c]
                    idx = idx + 1
                else : 
                    answer = answer + 1
                    
            newboard[r] = newc
        
        if not flag :
            break
            
    return answer


def rotate90(row,columm,board): 
    ret = [[0] * row for _ in range(columm)] 
    for r in range(row): 
        for c in range(columm):
            ret[c][row-1-r] = board[r][c]   
    return ret

def printTable(board):
    for i in board:
        for j in i:
            print(j,end='')
        print('')

print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))
print(solution(4 , 5, ["AAAAA","AUUUA","AUUAA","AAAAA"] ))
print(solution(6 , 6, ["AABBFF","AAAFFF","VAAFFV","AABBFF","AACCFF","VVCCFF" ] ))

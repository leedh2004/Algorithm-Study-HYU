def rotate90(key):
    return list(zip(*key[::-1]))
    
def attack(key,board,M,x,y):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detack(key,board,M,x,y):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def check(key,board,M,N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1 :
                return False
    return True

def solution(key, lock):
    M,N= len(key), len(lock)
    board = [ [0 for _ in range(2*M+N) ] for i in range(2*M+N) ] 
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    for _ in range(4):
        key = rotate90(key)
        for i in range(1, M+N):
            for j in range(1, M+N):
                attack(key,board,M,i,j)
                if check(key,board,M,N): 
                    return True
                detack(key,board,M,i,j)
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
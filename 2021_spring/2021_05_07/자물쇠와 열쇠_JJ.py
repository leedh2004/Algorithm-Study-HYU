def solution(key, lock):
    m,n = len(key),len(lock)
    homes = getlockList(lock)
    # print(homes)

    # 회전
    for _ in range(4):
        key = rotate90(m,m,key)

        # 축이동 
        for rowMove in range(-m+1,n):
            for colummMove in  range(-m+1,n):

                keys = []
                for row in range(m):
                    for columm in range(m):
                        m_row = rowMove+row
                        m_columm = colummMove + columm

                        if is_in(m_row,m_columm,n):
                            if key[row][columm] == 1:
                                keys.append([m_row,m_columm])
                # print(homes,keys)
                if homes == keys :
                    return True
    return False

def is_in(x,y,n):
    return 0<=x<n and 0<=y<n

def rotate90(row,columm,board): 
    ret = [[0] * row for _ in range(columm)] 
    for r in range(row): 
        for c in range(columm):
            ret[c][row-1-r] = board[r][c]   
    return ret

def getlockList(lock):
    n = len(lock)
    ret = []
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                ret.append([i,j])
    return ret
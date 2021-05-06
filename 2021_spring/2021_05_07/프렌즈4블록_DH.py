import copy
answer = 0
D = [(0, 0), (0, 1), (1, 0), (1, 1)]

def solution(m, n, b):
    global answer
    b = [ [ b[i][j] for j in range(n)] for i in range(m) ]

    # 지워지는 애들을 *로 바꿈
    def check():
        global answer
        new_b = copy.deepcopy(b)
        for y in range(m-1):
            for x in range(n-1):
                if b[y][x] == b[y+1][x] == b[y][x+1] == b[y+1][x+1] and b[y][x] != '*':
                    for dy, dx in D:
                        if new_b[y+dy][x+dx] != '*':
                            new_b[y+dy][x+dx] = '*'
                            answer += 1
        return new_b
    
    # 밑으로 내림
    def fall():
        for x in range(n):
            new_x = ""
            for y in range(m):
                if b[y][x] != '*':
                    new_x += b[y][x]
            new_x =  '*' * (m - len(new_x)) + new_x
            for y in range(m):
                b[y][x] = new_x[y]
            
    while True:
        flag = answer
        b = check()
        if flag == answer:
            break
        fall()
        
    return answer
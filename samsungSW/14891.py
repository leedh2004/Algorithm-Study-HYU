import sys

check= [False]*5

def turn_st(sawtooth,num,way):
    check[num] = True

    if num -1 > 0 and check[num-1] ==False: # turn left
        if sawtooth[num-1][2] != sawtooth[num][6]:
            turn_st(sawtooth,num-1,way*(-1))
    if num +1 < 5 and check[num+1] == False: #turn right
        if sawtooth[num+1][6] != sawtooth[num][2]:
            turn_st(sawtooth,num+1,way*(-1))

    if way == 1:
        turn_cw(sawtooth,num)
    elif way == -1:
        turn_ccw(sawtooth,num)
                
def turn_cw(sawtooth,num):
    tmp = sawtooth[num][7]
    for i in range(7,0,-1):
        sawtooth[num][i] = sawtooth[num][i-1]
    sawtooth[num][0] = tmp

def turn_ccw(sawtooth,num):
    tmp = 8sawtooth[num][0]
    for i in range(7):
        sawtooth[num][i] = sawtooth[num][i+1]
    sawtooth[num][7] = tmp

def check_score(sawtooth):
    score = 0
    for i in range(4):
        if sawtooth[i+1][0] == 1:
            score += (2 **i)
    return score

sawtooth = [[0]* 8 for _ in range(5)]

for i in range(1,5):
    line = sys.stdin.readline()
    for j in range(8):
        sawtooth[i][j] = int(line[j])

K = int(sys.stdin.readline())
turn = []
for i in range(K):
    n,w = map(int,sys.stdin.readline().split())
    turn.append((n,w))

for i in range(K):
    n,w = turn[i]
    turn_st(sawtooth,n,w)
    check = [False]*5
    
print(check_score(sawtooth))

        

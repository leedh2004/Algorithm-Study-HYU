import sys
                       
def turn_up(how,up,down,front,back,left,right):
    if(how == '-'):
        tmp = front[0]
        front[0][0] = left[0][2]
        front[0][1] = left[0][1]
        front[0][2] = left[0][0]
        left[0] = back[0]
        back[0][0] = right[0][2]
        back[0][1] = right[0][1]
        back[0][2] = right[0][0]
        right[0] = tmp
        spin('-',up)
    elif (how == '+'):
        tmp = front[0]
        front[0]= right[0]
        right[0][0] = back[0][2]
        right[0][1] = back[0][1]
        right[0][2] = back[0][0]
        back[0] = left[0]
        left[0][0] = tmp[2]
        left[0][1] = tmp[1]
        left[0][2] = tmp[0]
        spin('+',up)
def turn(how,up,down,front,back,left,right):
    if (how == 'U-'):
        turn_up('-',up,down,front,back,left,right)
    elif(how == 'U+'):
        turn_up('+',up,down,front,back,left,right)
    elif (how == 'F+'):
        rollback(up,down,front,back,left,right)
        turn_up('+',up,down,front,back,left,right)
    elif(how == 'F-'):
        rollback(up,down,front,back,left,right)
        turn_up('-',up,down,front,back,left,right)
    elif(how == 'D-'):
        rollback(up,down,front,back,left,right)
        rollback(up,down,front,back,left,right)
        turn_up('-',up,down,front,back,left,right)
    elif(how == 'D+'):
        rollback(up,down,front,back,left,right)
        rollback(up,down,front,back,left,right)
        turn_up('+',up,down,front,back,left,right)
    elif(how == 'B+'):
        rollback(up,down,front,back,left,right)
        rollback(up,down,front,back,left,right)
        rollback(up,down,front,back,left,right)
        turn_up('+',up,down,front,back,left,right)
    elif(how == 'B-'):
        rollback(up,down,front,back,left,right)
        rollback(up,down,front,back,left,right)
        rollback(up,down,front,back,left,right)
        turn_up('-',up,down,front,back,left,right)
    elif(how == 'L+'):
        turn_left(up,down,front,back,left,right)
        turn_up('+',up,down,front,back,left,right)
    elif(how == 'L-'):
        turn_left(up,down,front,back,left,right)
        turn_up('-',up,down,front,back,left,right)
        for i in range(3):
            print(right[i])
    elif(how == 'R+'):
        turn_left(up,down,front,back,left,right)
        turn_left(up,down,front,back,left,right)
        turn_left(up,down,front,back,left,right)
        turn_up('+',up,down,front,back,left,right)
    elif(how == 'R-'):
        turn_left(up,down,front,back,left,right)
        turn_left(up,down,front,back,left,right)
        turn_left(up,down,front,back,left,right)
        turn_up('-',up,down,front,back,left,right)
    
        
            

def spin(how,side):
    number = []
    for i in range(3):
        for j in range(3):
            number.append(side[i][j])
    if how == '+':
        side[0][0] = number[6]
        side[0][1] = number[3]
        side[0][2] = number[0]
        side[1][0] = number[7]
        side[1][2] = number[1]
        side[2][0] = number[8]
        side[2][1] = number[5]
        side[2][2] = number[2]
    elif how == '-':
        side[0][0] = number[2]
        side[0][1] = number[5]
        side[0][2] = number[8]
        side[1][0] = number[1]
        side[1][2] = number[7]
        side[2][0] = number[0]
        side[2][1] = number[3]
        side[2][2] = number[6]
        
def rollback(up,down,front,back,left,right):
    spin('-',left)
    spin('+',right)
    tmp = down
    down = back
    back[0] = up[2]
    back[1] = up[1]
    back[2] = up[0]
    up = front
    front[0] = tmp[2]
    front[1] = tmp[1]
    front[2] = tmp[0]

def turn_left(up,down,front,back,left,right):
    spin('-',back)
    spin('+',front)
    tmp = up
    up[0][0] = left[2][2]
    up[0][1] = left[1][2]
    up[0][2] = left[0][2]
    up[1][0] = left[2][1]
    up[1][1] = left[1][1]
    up[1][2] = left[0][1]
    up[2][0] = left[2][0]
    up[2][1] = left[1][0]
    up[2][2] = left[0][0]
    left = down
    spin('-',left)
    down[0][0] = right[2][2]
    down[0][1] = right[1][2]
    down[0][2] = right[0][2]
    down[1][0] = right[2][1]
    down[1][1] = right[1][1]
    down[1][2] = right[0][1]
    down[2][0] = right[2][0]
    down[2][1] = right[1][0]
    down[2][2] = right[0][0]
    right = tmp
    spin('+',right)



up = [['w']*3 for _ in range(3)]
down = [['y']*3 for _ in range(3)]
front = [['r']*3 for _ in range(3)]
back = [['o']*3 for _ in range(3)]
left = [['g']*3 for _ in range(3)]
right = [['b']*3 for _ in range(3)]

c = int(sys.stdin.readline())
case = []
for i in range(c):
    n = int(sys.stdin.readline())
    case = list(sys.stdin.readline().split())
    print(case)
    for j in range(n):
        turn(case[j],up,down,front,back,left,right)
    case.clear()
        



import sys

def quad_tree(i,j,span):
    global screen
    cur = screen[i][j]
    same = True

    for y in range(i,i+span):
        if same == False:
            break
        for x in range(j,j+span):
            if cur != screen[y][x]:
                same = False
                break
    
    if same:
        print(cur,end='')
    else:
        print("(",end='')
        new_span = span//2
        quad_tree(i,j,new_span)
        quad_tree(i,j+new_span,new_span)
        quad_tree(i+new_span,j,new_span)
        quad_tree(i+new_span,j+new_span,new_span)
        print(")",end='')

N = int(sys.stdin.readline())
screen = [[0]*N for _ in range(N)]
for i in range(N):
    line = sys.stdin.readline()
    for j in range(N):
        if line[j] == "1":
            screen[i][j] = 1
#for i in range(N):
#    print(screen[i])

quad_tree(0,0,N)



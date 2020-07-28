t = int(input())

while t>0:
    t = t -1
    p = []
    for i in range(4):
        x,y = map(int, input().split())
        p.append([x,y])

    for i in range(0,4):
        p[i].append( pow(p[0][0] - p[i][0],2) + pow(p[0][1] - p[i][1],2))
    
    #print(p)

    p = sorted(p, key=lambda p: p[2])

    #print(p)

    #and (p[0][0] + p[3][0]) / 2  == (p[1][0] + p[2][0]) / 2 and  (p[0][1] + p[3][1]) / 2  == (p[1][1] + p[2][1]) / 2

    if p[1][2] == p[2][2] and p[1][2]+p[2][2] == p[3][2] and (p[0][0] + p[3][0]) == (p[1][0] + p[2][0]) and  (p[0][1] + p[3][1])  == (p[1][1] + p[2][1]) :
        print(1)
    else :
        print(0)
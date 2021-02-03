T = int(input())

for i in range(T):
    x = list()
    y = list()
    d = list()
    for j in range(4):
        tmp_x,tmp_y = map( int,input().split() )
        x.append(tmp_x)
        y.append(tmp_y)
    for j in range(4):
        for k in range(j+1,4,1):
            d.append( (x[j]-x[k])**2 + (y[j]-y[k])**2 )
    d.sort()
    print(d)

    if(d[0]==d[1] and d[1]==d[2] and d[2]==d[3] and d[4]==d[5]):
        print(1)
    else:
        print(0)
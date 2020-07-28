import collections

c = int(input())

for i in range(c):
    flag = 1
    n = int(input())
    home_x, home_y = map( int,input().split() )
    
    con = list()  #편의점 위치 저장
    for j in range(n):
        c_x,c_y = map(int,input().split())
        con.append( [c_x,c_y,False] )
    con_len = len(con)
    
    
    des_x, des_y = map( int, input().split() ) #도착 위치 저장

    q = collections.deque()
    q.append( [home_x, home_y] )

    while q :
        x, y = q.popleft()
        tmp_dis = abs(x-des_x)+abs(y-des_y)

        if tmp_dis <= 50*20 :
            print("happy")
            flag = 0
            break
        
        for j in range(con_len) : 
            tmp_x,tmp_y,ch = con[j]
            if( (abs(x-tmp_x)+abs(y-tmp_y)) <= 50*20 and ch == False ) :
                q.append( [tmp_x,tmp_y] )
                con[j][2] = True
    
    if(flag == 1):
        print("sad")
import copy
def move(N,M,x,y,mat,ins,K) :
    dic = [0] * 6
    
    for i in range(K) :
        tmp_dic = copy.deepcopy(dic)
        if ins[i] == 1 :
            y += 1
            if y>=M :
                y -= 1
                continue
            dic[0] = tmp_dic[3]
            dic[2] = tmp_dic[0]
            dic[3] = tmp_dic[5]
            dic[5] = tmp_dic[2]
            
            if mat[x][y] == 0 :
                mat[x][y] = dic[5]
            elif mat[x][y] != 0 :
                dic[5] = mat[x][y]
                mat[x][y] = 0

        elif ins[i] == 2 :
            y -= 1
            if y<0 :
                y += 1
                continue
            dic[0] = tmp_dic[2]
            dic[2] = tmp_dic[5]
            dic[3] = tmp_dic[0]
            dic[5] = tmp_dic[3]
            
            if mat[x][y] == 0 :
                mat[x][y] = dic[5]
            elif mat[x][y] != 0 :
                dic[5] = mat[x][y]
                mat[x][y] = 0

        elif ins[i] == 3 :
            x -= 1
            if x<0 :
                x += 1
                continue
            dic[0] = tmp_dic[4]
            dic[1] = tmp_dic[0]
            dic[4] = tmp_dic[5]
            dic[5] = tmp_dic[1]
            
            if mat[x][y] == 0 :
                mat[x][y] = dic[5]
            elif mat[x][y] != 0 :
                dic[5] = mat[x][y]
                mat[x][y] = 0

        elif ins[i] == 4 :
            x += 1
            if x>=N :
                x -= 1
                continue
            dic[0] = tmp_dic[1]
            dic[1] = tmp_dic[5]
            dic[4] = tmp_dic[0]
            dic[5] = tmp_dic[4]
            
            if mat[x][y] == 0 :
                mat[x][y] = dic[5]
            elif mat[x][y] != 0 :
                dic[5] = mat[x][y]
                mat[x][y] = 0
        print(dic[0])


if __name__ == '__main__' :
    N,M,x,y,K = map(int, input().split())
    mat = [list(map(int,input().split())) for _ in range(N)]
    ins = list(map(int,input().split()))
    move(N,M,x,y,mat,ins,K)
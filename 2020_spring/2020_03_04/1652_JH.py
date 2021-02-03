N = int(input())
mat = [list(input()) for _ in range(N)]

def solve():
    global N
    global mat
    row = 0
    col = 0

    for i in range(N):
        for j in range(N):
            if mat[i][j] == '.':  #빈 공간 찾았다면
                count = 0
                for k in range(j,N,1): #왼쪽으로 가며 탐색, 오른쪽은 볼 필요 없음
                    if mat[i][k] == '.':
                        count += 1
                    if mat[i][k] == 'X':
                        break
                if count >= 2:
                    if j>0 :
                        if mat[i][j-1] != '.':
                            row +=1
                    else :
                        row += 1

                count = 0
                for k in range(i,N,1):
                    if mat[k][j] == '.':
                        count += 1
                    if mat[k][j] == 'X':
                        break
                if count >= 2:
                    if i>0:
                        if mat[i-1][j] != '.':
                            col += 1
                    else :
                        col += 1
    print(row, col)
solve()
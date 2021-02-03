import copy          #모르겠어용 ㅠㅠㅠ
def solve(tmp_white,tmp_mat,tmp_result):
    global result
    if not tmp_white :
        return 

    while tmp_white :
        x,y = tmp_white.pop(0)
        if tmp_mat[x][y] == 0 :
            continue 
        tmp_result +=1
        for i in range(4):
            nx,ny = x,y
            while nx>=0 and nx<N and ny>=0 and ny<N :
                tmp_mat[nx][ny] = 0
                nx,ny = nx+dx[i], ny+dy[i]
    
        solve(copy.deepcopy(tmp_white),copy.deepcopy(tmp_mat),tmp_result)
        result = max(result, tmp_result)
    
    



N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
white = []
dx = [1,1,-1,-1]
dy = [1,-1,1,-1]
result = 0

for i in range(N):
    for j in range(N):
        if mat[i][j] == 1 :
            white.append([i,j])

# result = solve(copy.deepcopy(white),copy.deepcopy(mat),0)
solve(copy.deepcopy(white),copy.deepcopy(mat),0)
print(result)






# import copy       그리디로 풀었더니 틀렸습니다.
# N = int(input())
# ori_mat = [list(map(int,input().split())) for _ in range(N)]
# dx = [1,1,-1,-1]
# dy = [1,-1,1,-1]
# ori_result = 0

# for a in range(N):
#     for b in range(N):
#         if(ori_mat[a][b] == 0):
#             continue
#         mat = copy.deepcopy(ori_mat)
#         result = 0
#         for i in range(a,N):
#             for j in range(b,N):
#                 if mat[i][j] == 1 :
#                     result += 1
#                     for k in range(4):
#                         x,y = i,j
#                         while x>=0 and x<N and y>=0 and y<N :
#                             mat[x][y] = 0
#                             x += dx[k]
#                             y += dy[k]
                            
#         ori_result = max(result, ori_result)
        

# print(ori_result)
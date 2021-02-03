def solve(N,x,y):    #사각형을 맨 처음부터 (1,1)부터
    global t_x, t_y, count
    if N == 2 :
        if x == t_x and y == t_y :
            print(count)
            return
        count += 1
        if x == t_x and y+1 == t_y :
            print(count)
            return
        count += 1
        if x+1 == t_x and y == t_y :
            print(count)
            return
        count += 1
        if x+1 == t_x and y+1 == t_y : 
            print(count)
            return
        count += 1
        return
    solve(N//2, x, y)
    solve(N//2, x, y+N//2)
    solve(N//2, x+N//2, y)
    solve(N//2, x+N//2, y+N//2)
            
N, t_x, t_y = map(int, input().split())
count = 0
solve(2**N,0,0)





# def solve(N,x,y):  #사각형을 맨 마지막 부터 (2,2)부터 왜 시간초과 ?
#     global count, t_x, t_y, check, result
#     if N == 1 :
#         x, y = x-1, y-1
#         for i in range(2):
#             nx = x+i
#             for j in range(2):
#                 ny = y+j
#                 count += 1
#                 if nx == t_x and ny == t_y :
#                     print(count)
#                     exit(0)
#                     return True
#         return False
#     else :                
#         check = solve(N-1, x//2, y//2)
#         if check == False :
#             check = solve(N-1,x//2, y)
#         if check == False :
#             check = solve(N-1,x, y//2)
#         if check == False :
#             solve(N-1,x,y)
#     return check

# N, t_x, t_y = map(int, input().split())
# t_x,t_y = t_x+1, t_y+1
# count = -1
# result = 0
# check = False
# solve(N,2**N,2**N)
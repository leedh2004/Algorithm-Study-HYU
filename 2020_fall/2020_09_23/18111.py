def solve(x,tmp):
    global N,M,mat
    time = 0
    for i in range(N):
        for j in range(M):
            cal = x - mat[i][j]
            abso = abs(cal)
            if cal < 0 :
                tmp += abso
                time += 2*abso
            elif cal >= 0 :
                tmp -= abso
                time += abso
    if tmp >= 0 :
        return time
    else :
        return 10e9

N, M, B = map(int,input().split())
mat = [ list(map(int,input().split())) for _ in range(N) ]
max_h, min_h = max(max(mat)), min(min(mat))
result1 = 10e9
result2 = -1
for i in range(min_h, max_h+1):
    tmp_result = solve(i,B)
    if result1 >= tmp_result :
        result1 = tmp_result
        result2 = max(result2, i)

print(result1, result2)

# def solve(x,y,tmp):    #시간초과
#     global N,M,mat
#     time = 0
#     for i in range(N):
#         for j in range(M):
#             cal = mat[x][y] - mat[i][j]
#             abso = abs(cal)
#             if cal < 0 :
#                 tmp += abso
#                 time += 2*abso
#             elif cal >= 0 :
#                 tmp -= abso
#                 time += abso
#     if tmp >= 0 :
#         return time
#     else :
#         return 10e9

# N, M, B = map(int,input().split())
# mat = [ list(map(int,input().split())) for _ in range(N) ]
# visit = [False for _ in range(257)]
# result1 = 10e9
# result2 = -1
# for i in range(N):
#     for j in range(M):
#         if visit[mat[i][j]] == False :
#             visit[mat[i][j]] = True
#             tmp = solve(i,j,B)
#             if result1 > tmp :
#                 result1 = tmp
#                 result2 = max(result2, mat[i][j])

# print(result1, result2)
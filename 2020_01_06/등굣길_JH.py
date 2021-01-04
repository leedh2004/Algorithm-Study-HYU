#가로 세로 첫줄은 무조건 갈 수 있다고 생각했었는데 아닌듯.(그렇게 짜면 실패 몇개 뜸)
def solution(m, n, puddles):
    mat = [[0 for _ in range(m)] for i in range(n)]
    result = 0
    for y,x in puddles :
        mat[x-1][y-1] = -1
    mat[0][0] = 1

    for i in range(0, n, 1):
        for j in range(0, m, 1):
            if mat[i][j] == -1 :
                mat[i][j] = 0
                continue
            if i != 0 :
                mat[i][j] += mat[i-1][j]
            if j != 0 :
                mat[i][j] += mat[i][j-1]

    result = mat[n-1][m-1]
    answer = result % 1000000007
    return answer

print(solution(4,3,[[2,2]]))



#정확성8 - 시간초과, 효율성 전부 실패
# from collections import deque
# def solution(m, n, puddles):
#     mat = [[1000 for _ in range(m)] for i in range(n)]
#     visit = [[False for _ in range(m)] for i in range(n)]
#     for y,x in puddles :
#         mat[x-1][y-1] = -1
#     mat[0][0] = 0
#     visit[0][0] = True
#     result = 0
#     dx,dy = [1,0], [0,1]
#     q = deque()
#     q.append([0,0])

#     while q :
#         for i in range(len(q)):
#             x,y = q.popleft()
#             for i in range(2):
#                 nx,ny = x+dx[i], y+dy[i]
#                 if nx>=0 and nx<n and ny>=0 and ny<m and mat[nx][ny] != -1 and visit[nx][ny] == False :
#                     if nx != n-1 or ny != m-1 :
#                         # visit[nx][ny] = True
#                         mat[nx][ny] = min(mat[nx][ny], mat[x][y]+1)
#                         q.append([nx, ny])

#                     else :
#                         if mat[nx][ny] > mat[x][y]+1 :
#                             mat[nx][ny] = mat[x][y]+1
#                             result = 1
#                         elif mat[nx][ny] == mat[x][y]+1 :
#                             result += 1
#                         else :
#                             result = result

#     for i in range(n):
#         print(mat[i])                    

#     answer = result % 1000000007
#     return answer

# print(solution(4,3,[[2,2]]))
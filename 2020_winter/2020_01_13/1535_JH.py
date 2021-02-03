#아래거랑 차이점이 뭔지 모르겠습니다. 제발 알려주세요 ㅠ
N = int(input())
L = list(map(int,input().split()))
J = list(map(int,input().split()))

c = list()
mat = [ [ 0 for _ in range(101) ] for i in range(N+1) ]

for i in range(1, N+1, 1):
    for j in range(1, 101, 1) :
        weight, value = L[i-1], J[i-1]
        if j > weight :
            mat[i][j] = max(mat[i-1][j-weight]+value, mat[i-1][j])
        else :
            mat[i][j] = mat[i-1][j]

print(mat[N][100])
            


# N = int(input())
# L = list(map(int,input().split()))
# J = list(map(int,input().split()))

# c = list()
# zero = 0 
# len_L = len(L)
# mat = [ [ 0 for _ in range(101) ] for i in range(len_L+1) ]

# for i in range( len(L) ):
#     if L[i] == 0 :
#         zero += J[i]
#     else :
#         c.append( (L[i], J[i]) )

# for index, (l, j) in enumerate(c):
#     for i in range(1, 101, 1):
#         if i > l :
#             mat[index+1][i] = max(mat[index][i], mat[index][i-l]+j)
#         else :
#             mat[index+1][i] = mat[index][i]

# print(mat[len_L][100] + zero )
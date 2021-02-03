# 이게 조금 더 빠르네용
import sys
input = sys.stdin.readline

N = int(input())
T = int(input())
mat = [ [0 for col in range(N)] for row in range(N) ]
cycle = N//2
how_many = cycle*2
count = N**2
T_row, T_col = cycle+1,cycle+1
mat[cycle][cycle] = 1

n_row, n_col = [1,0,-1,0], [0,1,0,-1]

for i in range(cycle):
    row_idx, col_idx = i,i
    for j in range(4):
        for k in range(how_many):
            mat[row_idx][col_idx] = count
            if count == T :
                T_row, T_col = row_idx+1, col_idx+1
            row_idx, col_idx = row_idx+n_row[j], col_idx+n_col[j]
            count -= 1
    how_many -= 2

for line in mat :
    print(*line)
print(T_row, T_col)



# import sys
# input = sys.stdin.readline

# N = int(input())
# T = int(input())
# mat = [ [0 for col in range(N)] for row in range(N) ]
# cycle = N//2
# how_many = cycle*2
# count = N**2
# T_row, T_col = cycle+1,cycle+1
# mat[cycle][cycle] = 1

# for i in range(cycle):
#     row_idx, col_idx = i,i
#     for j in range(how_many):
#         mat[row_idx][col_idx] = count
#         if count == T :
#             T_row, T_col = row_idx+1, col_idx+1
#         row_idx += 1
#         count -= 1
#     for j in range(how_many):
#         mat[row_idx][col_idx] = count
#         if count == T :
#             T_row, T_col = row_idx+1, col_idx+1
#         col_idx += 1
#         count -= 1
#     for j in range(how_many):
#         mat[row_idx][col_idx] = count
#         if count == T :
#             T_row, T_col = row_idx+1, col_idx+1
#         row_idx -= 1
#         count -= 1
#     for j in range(how_many):
#         mat[row_idx][col_idx] = count
#         if count == T :
#             T_row, T_col = row_idx+1, col_idx+1
#         col_idx -= 1
#         count -= 1
    
#     how_many -= 2


# for line in mat :
#     print(*line)
# print(T_row, T_col)
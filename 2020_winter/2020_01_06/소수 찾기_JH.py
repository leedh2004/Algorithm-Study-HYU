#이렇게 짜면 당연히 시간초과 날줄 알았는데... (순열로 경우의수 만들어서 set에 넣고 다 제곱근 수 전까지로 다 나눠보기)
from itertools import permutations
import math

def solution(numbers):
    result = []
    chars = list(numbers)

    for i in range(1, len(chars)+1):
        tmp_case = set(map(''.join,permutations(chars,i)))
        for j in tmp_case :
            j = int(j)
            flag = 1
            if j < 2 :
                continue
            else :
                for k in range(2, int( math.sqrt(j) )+1) :
                    if j % k == 0 :
                        flag = 0

                if flag :
                    result.append(j)

    answer = len(set(result))
    return answer

print(solution("17"))




#dfs로 완전 탐색 후 factorial로 소수 체크 했으나 실패 & 시간초과 뜸
# import copy

# def dfs(start, tmp_list) :
#     global mat, result

#     if int(start) != 0 and int(start) != 1 :
#         if( (mat[int(start)-1]+1)%int(start) == 0 ) :
#             result += 1
    
#     if not tmp_list :
#         return

#     for i,c in enumerate(tmp_list) :
#         tmp_list2 = copy.deepcopy(tmp_list)
#         tmp_list2.pop(i)
#         dfs(start+c, tmp_list2)
    


# def fact_init(numbers):
#     global mat
#     chars = list(numbers)
#     chars.sort(reverse = True)
#     char_dic = dict()
#     mat_range = ''.join(chars)
#     mat = [1 for _ in range(int(mat_range)+1)]

#     for i in range(1,int(mat_range)+1):
#         mat[i] = i*mat[i-1]

# numbers = "011"

# chars = list(numbers)
# chars.sort(reverse = True)
# char_dic = dict()
# mat_range = ''.join(chars)
# mat = list()
# fact_init(numbers)
# # mat = [1 for _ in range(int(mat_range)+1)]

# # for i in range(1,int(mat_range)+1):
# #     mat[i] = i*mat[i-1]

# result = 0
# for i in range(10):
#     char_dic[str(i)] = False

# char_dic['0'] = True

# for i,c in enumerate(chars) :
#     if char_dic[c] == True :
#         continue
    
#     char_dic[c] = True
#     tmp_list = copy.deepcopy(chars)
#     tmp_list.pop(i)
#     dfs(c, tmp_list)

# print(result)

# import copy

# mat = list()
# result = 0

# def fact_init(numbers):
#     global mat
#     chars = list(numbers)
#     chars.sort(reverse = True)
#     char_dic = dict()
#     mat_range = ''.join(chars)
#     mat = [1 for _ in range(int(mat_range)+1)]

#     for i in range(1,int(mat_range)+1):
#         mat[i] = i*mat[i-1]


# def dfs(start, tmp_list) :
#     global mat, result, count

#     if int(start) != 0 and int(start) != 1 :
#         if( (mat[int(start)-1]+1)%int(start) == 0 ) :
#             result += 1
    
#     if not tmp_list :
#         return

#     for i,c in enumerate(tmp_list) :
#         tmp_list2 = copy.deepcopy(tmp_list)
#         tmp_list2.pop(i)
#         dfs(start+c, tmp_list2)

# def solution(numbers):
#     global mat, result
#     chars = list(numbers)
#     chars.sort(reverse = True)
#     char_dic = dict()
#     fact_init(numbers)

#     for i in range(10):
#         char_dic[str(i)] = False

#     char_dic['0'] = True

#     for i,c in enumerate(chars) :
#         if char_dic[c] == True :
#             continue

#         char_dic[c] = True
#         tmp_list = copy.deepcopy(chars)
#         tmp_list.pop(i)
#         dfs(c, tmp_list)

#     answer = str(result)
#     return answer

# print(solution("17"))
#함수로 만들어서 바로 제출함
number =  '1231234'
k = 3

tmp_result = []

for i, char in enumerate(number) :
    for j in range(len(tmp_result)-1, -1, -1):
        if char > tmp_result[j] and k>0 :
            tmp_result.pop()
            k -= 1
        else :
            break
    if k == 0:
        tmp_result += number[i:]
        break
    tmp_result.append(char)

if k > 0:
    tmp_result = tmp_result[:-k]
answer = "".join(tmp_result)
print(answer)
    





#4개 통과 나머지 시간초과
# from itertools import combinations

# number =  '1924'
# k = 2
# chars = []

# for i, c in enumerate(number) :
#     chars.append([i,c])

# all_case = list(combinations(chars, len(chars)-k))

# result = -1

# for i in all_case : 
#     tmp_result = ''
#     for j in i :
#         tmp_result += j[1]
#     result = max(result, int(tmp_result))
# answer = str(result)
# print(answer)
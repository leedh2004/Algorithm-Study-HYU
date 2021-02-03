from functools import reduce
N = input()  #join함수 써보기, 30은 3의 배수에 마지막자리의 숫자가 0이면 됨, 3의 배수는 자리수 다 더해서 3의 배수, 3의 배수는 자릿수 다 합쳐서 3의 배수면 됨
L = list(str(N)) # 999을 입력 받으면 ['9','9','9']로 쪼개줌
a = 10**(len(L)-1)
L = sorted(L,reverse=True) #가장 큰 수니까 내림차순으로 정렬해줌
s = reduce(lambda x,y : int(x)+int(y),L)  #리스트 안의 요소를 모두 더해서 값 한개로

if L[-1] != "0" or s%3!=0 :
    print(-1)
else :
    print(int("".join(L)))  #리스트 안의 요소를 합치는 함수, 하고나서 형변환 해줌


   




# N = input()      #join 함수 안쓰고 int로 해결함
# L = list(map(int,str(N)))
# l = len(L)
# a = 10**(l-1)
# L = sorted(L,reverse=True)
# if L[-1] != 0 :
#     print(-1)
# else :
#     result = 0
#     for i in range(l):
#         result += L[i]*a
#         a//=10
#     print(result)
    






# import itertools   #메모리초과 뜸
# N = input()
# L = list(map(int,str(N)))
# a = 10**(len(L)-1)
# P = list(itertools.permutations(L))
# result = -1

# for i in range(len(P)):
#     tmp = 0
#     b = a
#     for j in range(len(P[i])):
#         tmp += P[i][j]*(b)
#         b//=10
#     if tmp%30 == 0 :
#         result = max(result,tmp)
# print(result)
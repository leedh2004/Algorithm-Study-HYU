# import math
# N,M = map(int,input().split())
# a = 1
# for i in range(N,N-M,-1):
#     a*=i 
# # result = a//math.factorial(M)
# # result = (math.factorial(N))//(math.factorial(N-M)*math.factorial(M))
# i = 10
# count = 0
# while True:
#     if result%i == 0:
#         count +=1
#     else :
#         break
#     i*=10
# print(count)


N,M = map(int,input().split())

def howMany(N,T):
    count = 0 
    while True:
        if N == 0:
            return count
        N = N//T   #처음에 나누는게 2의 배수의 갯수, 그다음에 나누는게 4의 배수의 갯수(2를 2개 가지고있음) 그다음이 8의 배수의 갯수(2를 3개 가지고 있음)....
        count += N

print(min(howMany(N,2)-howMany(N-M,2)-howMany(M,2) , howMany(N,5)-howMany(N-M,5)-howMany(M,5) ))
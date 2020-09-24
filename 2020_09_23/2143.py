T = int(input())   #메모리가 적다고 겁먹지 말자
N = int(input())
A = list(map(int, input().split())) 
M = int(input())
B = list(map(int, input().split())) 
SA = {}
SB = {}
result = 0

for i in range(N):
    tmp = 0
    for j in range(i,N):
        tmp += A[j]
        if SA.get(tmp):
            SA[tmp] += 1
        else :
            SA[tmp] = 1

for i in range(M):
    tmp = 0
    for j in range(i,M):
        tmp += B[j]
        if SB.get(tmp):
            SB[tmp] += 1
        else :
            SB[tmp] = 1

for i in SA :
    if SB.get(T-i):
        result += SB[T-i] * SA[i]

print(result)




# # T = int(input())
# # N = int(input())
# # A = list(map(int,input().split()))
# # A.sort()
# # M = int(input())
# # B = list(map(int,input().split()))
# # B.sort()

# # # for i in range(N) :
# # #     if A[i]+B[0]>T :
# # #         A = A[0:i]
# # #         break
# # # for i in range(M) :
# # #     if B[i]+A[0]>T :
# # #         B = B[0:i]
# # #         break
# # SA = []
# # SB = []
# # tmp = A[0]
# # for i in range(1,len(A)) :
# #     if tmp < tmp[i] :
        

A,B = input().split()  #A를 한칸씩 밀면서 하는 방법
A = list(A)  #문자열을 ['a',a',....] 이렇게 만듬
B = list(B)
LB = len(B)
LA = len(A)
result = 51

for i in range(LB-LA+1): #뒤에 붙였을때, 앞에 붙였을때
    tmp = 0 
    for j in range(LA):
        if A[j] != B[i+j]:
            tmp += 1
    result = min(result,tmp)

print(result)
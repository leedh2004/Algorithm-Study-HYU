from functools import reduce
import operator
L = [1]*10
N = int (input())


for i in range(1,N):
    for j in range(10) : #0~9값 초기화
        for k in range(j+1,10,1):
            L[j] += L[k]

print(reduce(operator.add,L,0)%10007)
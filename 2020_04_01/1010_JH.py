from itertools import combinations
from functools import reduce
import operator

def nCr(n,r):
    r = min(n-r,r) #nCr과 nCn-r은 같으므로 둘중 적은 값을 이용하기 위해
    numerator = reduce(operator.mul,range(n,n-r,-1),1)  #분자    파이썬에서 곱 연산을 가장 빠르게 할 수 있는 방법
    denominator = reduce(operator.mul,range(r,0,-1),1)   #분모
    print(numerator//denominator)

T = int(input())

for i in range(T):
    N,M = map(int,input().split())
    nCr(M,N)
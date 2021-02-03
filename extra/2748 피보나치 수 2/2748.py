import time
import sys
start = time.time()  # 시작 시간 저장
def fibonazzi(n):
    if n==0: return 0
    if n==1: return 1

    f_1 = 0
    f_2 = 1
    for i in range(n-1):
        f_n = f_1+f_2
        tmp = f_2
        f_1 = tmp
        f_2 = f_n
    return f_n
    
n = int(input())
print(fibonazzi(n))

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

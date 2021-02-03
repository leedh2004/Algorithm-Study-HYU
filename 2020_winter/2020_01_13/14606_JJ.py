import sys

def recur(num):

    # 종료 조건
    if num == 1 :
        return 0
    
    # 메모제이션이 되어있을때
    if dp[num] != -1 : 
        return dp[num]

    # num 짝수 홀수 여부
    if num%2 ==0:
        dp[num] =  (num//2) * (num//2) + recur(num//2) + recur(num//2) 
    else :  
        dp[num] =  (num//2) * (num - num//2) + recur(num//2) + recur(num - num//2) 
    return dp[num]
    
    

sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())
dp = [ -1 for row in range(n+1)]
print(recur(n))
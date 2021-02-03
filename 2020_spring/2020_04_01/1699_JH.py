import math  #99999 시간 찍어보면 12초 걸리는데 왜 맞는지 모르겠넹

N = int(input())
dp = [0]*(N+1) #직관적으로 편하게 이해하기 위해 그 숫자는 배열의 그 숫자 인덱스에 넣기로함 ex) 1->dp[1]

for i in range(1,N+1,1):
    s = int(math.sqrt(i))
    if s*s == i: #제곱수인 경우
        dp[i] = 1
    else : #제곱수가 아닌 경우, 제곱근의 소숫점 버린 값의 수부터 시작해서 가장 작은 값을 찾음
        m=9999999
        for j in range(s,0,-1):
            m = min(m,dp[i-(j*j)])
        dp[i] = m+1
print(dp[N])








# import math   #11,7은 잘 되는데 99999 하면 4가 아닌 6나옴

# N = int(input())
# dp = [0]*(N+1) #직관적으로 편하게 이해하기 위해 그 숫자는 배열의 그 숫자 인덱스에 넣기로함 ex) 1->dp[1]

# for i in range(1,N+1,1):
#     s = int(math.sqrt(i))
#     if s*s == i: #제곱수인 경우
#         dp[i] = 1
#     else : #제곱수가 아닌 경우, 제곱근의 소숫점 버린 값의 수의 제곱을 포함하고(+1), 남은 수 중 최적의 값 더 해주면 이 수 역시 최적화
#         dp[i] = dp[i-(s*s)] +1
# print(dp[N])
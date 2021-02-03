P = list(map(float, input().split()))
DP = [ [0 for _ in range(3051)] for i in range(21) ]
DP[0][2000] = 1

for i in range(1,21,1):
    for j in range(1000, 3001, 50):
        DP[i][j] += DP[i-1][j-50]*P[0]
        DP[i][j] += DP[i-1][j]*P[2]
        DP[i][j] += DP[i-1][j+50]*P[1]

for i in range(5):
    print( format( round( sum(DP[20][1000+(i*500):1500+(i*500)]) ,8), '0.8f' )  )


#시간초과 뜸, 혹시 잘못푼거임 ??
# P = list(map(float, input().split()))
# result = [0 for _ in  range(5)]
# get = [50, -50, 0]

# def solution(count, now_p, score):  #몇판 했는지, 지금까지의 확률, 지금까지의 점수
#     global P,result,get
#     if now_p == 0 :
#         return
#     if count == 20 :
#         if score>=1000 and score<=1499 :
#             result[0] += now_p
#         elif score>=1500 and score<=1999:
#             result[1] += now_p
#         elif score>=2000 and score<=2499:
#             result[2] += now_p
#         elif score>=2500 and score<=2999:
#             result[3] += now_p
#         else :
#             result[4] += now_p

#         return
    
#     for i in range(3):
#         solution(count+1, now_p*P[i], score+get[i])

# solution(0, 1, 2000)
# for i in range(5):
#     print(format( round(result[i],8), '0.8f') )
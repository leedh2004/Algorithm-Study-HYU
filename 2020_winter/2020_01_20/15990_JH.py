import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline   # 이거 안하면 시간초과 납니다. (그냥 input 함수 쓰면)

T = int(input())
DP = [ [0,0,0,0] for _ in range(100001) ]
DP[1][0], DP[1][1] = 1, 1
DP[2][0], DP[2][2] = 1, 1
DP[3][0] = 3
for i in range(1,4,1) :
    DP[3][i] = 1

def solution(i):
    global DP
    if DP[i][0] != 0 :
        return
    if DP[i-1][0] == 0 :
        solution(i-1) 

    for j in range(1,4,1):
        for k in range(1,4,1):
            if j == k :
                continue
            DP[i][j] =  (DP[i][j] + DP[i-j][k]) % 1000000009
            DP[i][0] =  (DP[i][0] + DP[i-j][k]) % 1000000009

for a in range(T):
    n = int(input())
    solution(n)
    print(DP[n][0])








# def solution(max_n):
#     global DP
#     if DP[max_n][0] != 0 :
#         return DP[max_n][0]

#     for i in range(4, 100001, 1) :
#         tmp_result = 0
#         for j in range(1,4,1):
#             for k in range(1,4,1):
#                 if j == k :
#                     continue
#                 # print(i,j,k)
#                 DP[i][j] += DP[i-j][k]
#                 tmp_result += DP[i-j][k]
#                 tmp_result %= 1000000009
#         DP[i][0] = tmp_result
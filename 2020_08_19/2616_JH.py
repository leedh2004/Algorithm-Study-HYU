N = int(input())
l = list(map(int,input().split()))
k = int(input())
s = [0 for _ in range(N+1)]
dp = [[0 for _ in range(N+1)] for _ in range(4)]
for i in range(N):
    s[i+1] = s[i]+l[i]

for i in range(1,4):
    for j in range(i*k,N+1):
        dp[i][j] = max(dp[i][j-1], s[j]-s[j-k]+dp[i-1][j-k])

print(dp[3][N])






# def solve(count, start, result):  시간초과
#     global final, l, N, s
#     if count == 3 :
#         return 
#     result[count] = 0
#     for i in range(start,N-s+1,1):        
#         result[count] = 0

#         for j in  range(s):
#             result[count] += l[i+j]

#         if(i+s<N+1):
#             solve(count+1, i+s, result)
#         final = max(final, result[0]+result[1]+result[2])
#         # print(result)


# N = int(input())
# l = list(map(int,input().split()))
# s = int(input())
# final = -1

# solve(0,0,[0,0,0])
# print(final)
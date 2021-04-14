import sys
input = sys.stdin.readline

H,Y = map(int,input().strip().split())
percent = { 1:1.05, 3:1.2, 5:1.35 }
DP = [ [0,0,0] for _ in range(Y+1)]
DP[0][0], DP[0][1], DP[0][2] = H, H, H

for i in range(1, Y+1, 1):
    if i-1 >= 0 :
        DP[i][0] = int(max(DP[i-1])*percent[1])
    else :
        DP[i][0] = DP[i-1][0]

    if i-3 >= 0 :
        DP[i][1] = int(max(DP[i-3])*percent[3])
    else :
        DP[i][1] = DP[i-1][1]

    if i-5 >= 0 :
        DP[i][2] = int(max(DP[i-5])*percent[5])
    else :
        DP[i][2] = DP[i-1][2]

# print(DP)
print(max(DP[Y]))




# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def solution(money, year):
#     global percent, DP
    
#     if year == 0 :
#         DP[year] = max(DP[year], money)
#         return DP[year]

#     if DP[year] != 0 :
#         return DP[year]

#     for next_year in percent :
#         if year-next_year >= 0 :
#             DP[year] =  max( DP[year], solution(int(money*percent[next_year]), year-next_year))

#     return DP[year]
        


# H,Y = map(int,input().strip().split())
# percent = { 1:1.05, 3:1.2, 5:1.35 }
# DP = [0 for _ in range(Y+1)]

# solution(H,Y)
# print(DP)
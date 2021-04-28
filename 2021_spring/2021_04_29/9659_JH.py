import sys
N = int(input().strip())
if N%2 == 0 :
    print('CY')
else :
    print('SK')


# 이게 시간초과가 뜨네요...
# import sys
# input = sys.stdin.readline
# from collections import deque

# N = int(input())
# ME, OTHER = "me", "other"
# DP = deque([ME, OTHER, ME])

# for i in range(4, N+1, 1):
#     one = DP.popleft()
#     three = DP[-1]

#     if one == OTHER or three == OTHER :
#         DP.append(ME)
#     else :
#         DP.append(OTHER)

# if DP[-1] == ME :
#     print("SK")
# else :
#     print("CY")
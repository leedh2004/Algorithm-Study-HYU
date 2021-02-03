#모르겠슴니당..

# import sys
# import math
# input = sys.stdin.readline

# def cal_dis(x,y):
#     resutl = 0 
#     for i in range(3) :
#         result += (x[i]-y[i])**2
#     result = math.sqrt(result)
#     return result

# L = list(map(int,input().split()))
# left,right,C = L[0:3], L[3:6], L[6:9]

# while left[0] <= right[0] :
#     p = [ left[i]*(2/3) + right[i]*(1/3) for i in range(3)  ]
#     q = [ left[i]*(1/3) + right[i]*(2/3) for i in range(3)  ]

#     fp, fq = cal_dis(C,p), cal_dis(C,q)

#     if fp >= fq :
#         left = p
#     else :
#         right = q




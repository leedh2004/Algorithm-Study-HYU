#B를 정렬하지 않고
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
result = 0

for i in range(len(A)):
    result += A[i]*B.pop(B.index(max(B)))

print(result)


#B를 정렬한 것
# N = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# A.sort()
# B.sort(reverse=True)

# result = 0

# for i in range(len(A)):
#     result += A[i]*B[i]

# print(result)

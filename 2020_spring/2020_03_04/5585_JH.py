N = int(input())
M = 1000 - N
L = [500, 100, 50, 10, 5, 1]
result = 0
for i in range(len(L)):
    result += M//L[i]
    M = M%L[i]
print(result)
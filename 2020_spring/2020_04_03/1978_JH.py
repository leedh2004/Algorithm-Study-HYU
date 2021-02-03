mat = [True]*1001
mat[0] = False
mat[1] = False
N = int(input())
L = list(map(int,input().split()))
result = 0

for i in range(2,1001,1):
    if mat[i] == True :
        for j in range(2,501,1):
            if i*j<=1000 and mat[i*j] == True:
                mat[i*j] = False
for i in L:
    if mat[i] == True:
        result += 1
print(result)
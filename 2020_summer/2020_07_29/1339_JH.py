N = int(input())
L = [0 for _ in range(26)]
result = 0
num = 9

for i in range(N):
    tmp =  input()
    posnum = 1
    for j in range(len(tmp)-1,-1,-1) :
        L[ord(tmp[j])-65] += posnum
        posnum *= 10

L.sort(reverse=True)

for i in L :
    result += i*num
    num -= 1

print(result)
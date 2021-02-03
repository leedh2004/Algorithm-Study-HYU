N = int(input())
mat = [0 for i in range(11)]

for i in range(1, 11, 1):
    k = i//2
    mat[i] = (i-k) * k
result = 0


#이쁘게 쓰는 법 알려주세요
def solution(n):
    global result, mat
    if n == 1 :
        return

    k = n//2
    result += mat[n]
    solution(k)
    solution(n-k)
    

solution(N)
print(result)
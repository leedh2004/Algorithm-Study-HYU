N = int(input())
F = int(input())

start = N//100   #끝에 두자리 0으로 만들고 1씩 증가시키면서 답 찾을거임
start *= 100

while start%F != 0 :
    start+=1
print(str(start)[-2:])
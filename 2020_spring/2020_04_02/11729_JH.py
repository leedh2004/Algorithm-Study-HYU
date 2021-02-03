N = int(input())
sum = 1

for i in range(N-1):
    sum = sum*2+1

def solve(n,f,s,t):
    if n == 1:
        print(f,t)
    else :
        solve(n-1,f,t,s) #first꺼를 second로 옮기고
        print(f,t)  #first의 가장 아래 원판을 third로 옮기고
        solve(n-1,s,f,t) #second의 원판을 third로 옮겨라 
        #즉 solve(n,a,b,c)가 있다면 a와 c의 자리를 바꿔주는거임, b는 신경 ㄴㄴ

print(sum)
solve(N,1,2,3)
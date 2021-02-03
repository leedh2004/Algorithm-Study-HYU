N = input()   #디버깅 코드를 잘지우자...
l = len(N)-1 
result = 0

for i in range(l):
    result+=9*(10**i)*(i+1)  #이전 수들의 자리수 총합
result += ((int(N)-(10**l))+1)*(l+1) #남은 수(120이면 100부터 120까지)*자릿수
print(result)
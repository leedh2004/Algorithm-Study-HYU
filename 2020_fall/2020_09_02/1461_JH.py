N,M = map(int, input().split())
l = list(map(int,input().split()))
minus =  list()
plus = list()
result = 0
min_minus = 0
max_plus = 0

for i in range(len(l)):
    if l[i] < 0 :
        minus.append(l[i])
    else :
        plus.append(l[i])
minus.sort()
plus.sort(reverse  = True)

for i in range(0,len(minus),M):
    result -= minus[i]*2
for i in range(0,len(plus),M):
    result += plus[i]*2

if minus :
    min_minus = -min(minus)
if plus :
    max_plus = max(plus)
result -= max(min_minus,max_plus)
    
print(result)
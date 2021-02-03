n = int(input())
l = list(map(int,input().split()))
result = 0

while True :
    m = max(l)
    i = l.index(m)
    if len(l) == 1 :
        break
    if i==0 :
        result += l[i]-l[i+1]
    elif i == len(l)-1 : 
        result += l[i]-l[i-1]
    else :
        left = l[i]-l[i-1]
        right = l[i]-l[i+1]
        result += min(left,right)
    l.pop(i)
print(result)
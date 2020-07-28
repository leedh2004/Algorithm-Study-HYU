N, M = map(int,input().split())
left = 0
money = []
for i in range(N):
    tmp = int(input())
    if tmp>left:
        left = tmp
    money.append(tmp)
right = sum(money)
result = 9999999

while left<=right:
    mid = (left+right) // 2
    tmp = mid
    count = 1
    for i in range(N):
        if (money[i] > tmp):
            count += 1
            tmp = mid
        
        tmp -= money[i]

    if(count > M):
        left = mid+1
    else :
        if(result > mid):
            result = mid
        right = mid-1
    
print(result)
l = int(input())
dt = list(map(int,input().split()))
n = int(input())

max_num = min(dt)
min_num = max(dt)

flag = False

for i in dt:
    if i > max_num and i < n:
        max_num = i
    if i < min_num and i > n:3
        min_num = i
    if i == n:
        flag = True
        break

if max_num>n:
    max_num = 0

max_num = max_num
min_num = min_num 

if flag :  
    print(0)
else :
    ans = (n - max_num) * (min_num - n) - 1
    print(ans)
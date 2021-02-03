j = int(input())
a = int(input())
size = [0]*j
check = [0]*j
for i in range(j):
    size[i] = str(input())
ans = 0
for i in range(a):
    tmp = list(input().split())
    if check[int(tmp[1])-1] == 0 and size[int(tmp[1])-1] <= tmp[0]:
        ans = ans +1 
        check[int(tmp[1])-1] = 1
print(ans)



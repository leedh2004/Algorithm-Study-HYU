N = int(input())
lis = list(map(int, (input().split())))
lis += [0, 0]
ans = 0
for idx, val in enumerate(lis):
    if idx >= N:
        break 
    if lis[idx] == 1:
        lis[idx] = 0 
        lis[idx+1] = 1 - lis[idx+1]
        lis[idx+2] = 1 - lis[idx+2]
        ans += 1
print(ans)
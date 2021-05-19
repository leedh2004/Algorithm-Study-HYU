T = int(input())
for _ in range(T):
    _ = input()
    a = sorted(list(map(int, input().split())))
    b = [-1] * len(a)
    start = 0
    end = len(a) - 1 
    turn = True 
    cnt = 0
    while start <= end:
        if turn:
            b[start] = a[cnt]
            start += 1
        else:
            b[end] = a[cnt]
            end -= 1
        turn = not turn
        cnt += 1
    b = b + [b[0]]
    ans = 0
    for i in range(len(b)-1):
        ans = max(ans, abs(b[i] - b[i+1]))
    print(ans)
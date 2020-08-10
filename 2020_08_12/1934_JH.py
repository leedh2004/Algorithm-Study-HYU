T = int(input())

for i in range(T):
    A, B = map(int, input().split())

    target = max(A,B)
    other = min(A,B)

    while True :
        quo = target//other
        rema = target%other
        if rema ==  0:
            break
        target = other
        other = rema
        
    print(A//other*B)
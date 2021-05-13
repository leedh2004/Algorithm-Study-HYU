T = int(input())

for _ in range(T):
    _ = input()
    A = list(map(int, input().split()))
    _ = input()
    B = list(map(int, input().split()))
    D = {}
    for a in A:
        D[a] = 1
    for b in B:
        if b in D:
            print(1)
        else:
            print(0)


N = int(input())
SK_WIN = [False] * 1001
SK_WIN[1] = SK_WIN[3] = SK_WIN[4] = True
for i in range(5, N+1):
    if SK_WIN[i-1] and SK_WIN[i-3] and SK_WIN[i-4]:
        SK_WIN[i] = False
    else:
        SK_WIN[i] = True
print("SK" if SK_WIN[N] else "CY")

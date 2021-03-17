import sys
input = sys.stdin.readline

idx = 1

while True :
    L,P,V = map(int, input().split())
    if L == 0 and P == 0 and V == 0 :
        break

    quo, re = V//P, V%P
    re = min(L, re)

    print('Case %d: %d'%(idx, L*quo+re))
    idx += 1
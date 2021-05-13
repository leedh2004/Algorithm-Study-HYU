import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    L1 = { i : True for i in list(map(int,input().strip().split()))  }
    M = int(input().strip())
    L2 = list(map(int,input().strip().split()))


    for i in L2 :
        try : 
            if L1[i] :
                print(1)
        except KeyError :
            print(0)
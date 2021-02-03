L = int(input())
lset = list(map(int,input().split()))
N = int(input())

lset.sort()

left = 0

for i in range(L):
    if(lset[i]==N):
        print(0)
        break

    if(lset[i]>N):
        if(i-1>=0):
            left = lset[i-1]
        print( (N-left)*(lset[i]-N)-1 )
        break
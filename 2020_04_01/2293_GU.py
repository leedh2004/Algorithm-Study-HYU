import sys

N,K = map(int,sys.stdin.readline().split())
d = [0] * 10001
coin =[]
cnt = 0
for i in range(N):
    coin.append(int(sys.stdin.readline()))
#coin.sort(reverse = True)
coin.sort()
d[0]=1
for i in range(len(coin)):
    for j in range(coin[0],K+1):
        if(j>=coin[i]):
            d[j] += d[j-coin[i]]

print(d[K])


"""N,K = map(int,sys.stdin.readline().split())
d = [0] * 10001
coin =[]
cnt = 0
for i in range(N):
    tmp = int(sys.stdin.readline())
    coin.append(tmp)
    d[tmp]=1

coin.sort()
#d[coin[0]]=1
for i in range(coin[0]+1,K+1):
    for j in range(len(coin)):
        if(i-coin[j] !=0):
            d[i] = d[i-coin[j]] +1
            break

print(d[K])"""


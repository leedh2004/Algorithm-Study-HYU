#2352 - 반도체 설계

import copy    #시간초과 나네용 ㅠ
def check(n,tmp,pre_connect):
    global N,result
    global port
    connect = copy.copy(pre_connect)

    # print("first")
    # print(connect)
    if n == N :
        result = max(result,tmp)
        return

    if connect[port[n]-1] == True :
        for i in range(port[n]-1,-1,-1):
            connect[i] = False
        tmp+=1
        # print("second")
        # print(connect)
    else :
        return

    for i in range(n+1,N+1,1):
        # print("i")
        # print(i)
        check(i,tmp,connect)


N = int(input())
port = list( map(int,input().split()) )
connect = [True for _ in range(N)]
result = -1

for i in range(N):
    check(i,0,connect)

print(result)
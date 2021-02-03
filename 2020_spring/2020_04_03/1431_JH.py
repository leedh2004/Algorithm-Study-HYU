import queue  #pypy에선 맞음, python에서는 런타임 에러 .... 왜 ?

N = int(input())
q = queue.PriorityQueue()
for i in range(N):
    l = 0 #문자열 길이 저장
    s = 0 #문자열의 숫자 합
    tmp = str(input())
    for j in tmp :
        l += 1
        if j.isdigit() :
            s += int(j)
    q.put((l,s,tmp))

for i in range(N):
    l,s,name = q.get()
    print(name)
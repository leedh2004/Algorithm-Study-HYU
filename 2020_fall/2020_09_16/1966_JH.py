T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    L = list(map(int,input().split()))
    count = 0  #출력횟수

    while L  :
        target = L.pop(0)
        flag = True

        for i in L:
            if i > target :
                flag = False
                break

        if flag :  #맨앞의 놈을 출력 할 수 있는 상태
            count += 1
            if M == 0 :   #맨앞의 놈이 우리가 원하는거면 count 출력하고 끝
                print(count)
                break
            else :   #맨앞의 놈이 우리가 원하는게 아니면 count += 1 하고 M의 인덱스 줄여주면 됨
                M -= 1

        else : #맨앞의 놈을 출력 할 수 없는 상태
            if M == 0 : #맨앞에 우리가 원하는게 있지만 출력할 수 없는 상태
                M = len(L)
            else : #맨앞에 우리가 원하는것도 아니고 출력할 수도 없는 상태
                M -= 1
            L.append(target) #출력 할 수 없는 상태니까 다시 맨 뒤로 보내줘야함
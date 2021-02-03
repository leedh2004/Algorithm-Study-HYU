import queue     #시간초과 뜸
N = int(input())
front = queue.PriorityQueue() #mid보다 작은 수들 모임
back = queue.PriorityQueue() #mid보다 큰 수들 모임
idx1 = 0 #front의 인덱스
idx2 = 0 #back의 인덱스
mid = (0,0)  #가운데 수
for i in range(N):
    num = int(input())
    if num<=mid[1]:
        front.put_nowait((-num,num))  #priority가 낮은 순으로 자동 정렬해주니까, priority를 음수 취해서 넣어주면 높은값이 제일 처음
        idx1 += 1
    else :
        back.put_nowait((num,num))
        idx2 += 1

    while True:  #좌우의 균형을 맞춰줌. 그리고 front의 첫번째 꺼 보면 중간값
        if idx1>=idx2:
            break
        tmp = back.get_nowait()
        front.put_nowait((-tmp[1],tmp[1]))
        idx1 += 1
        idx2 -= 1
    mid = front.get_nowait()
    print(mid[1])
    front.put_nowait((-mid[1],mid[1]))






# N = int(input())   #시간초과
# L = list()
# idx = 0 
# for i in range(N) :
#     L.append(int(input()))
#     L.sort()
#     print(L[idx//2])
#     idx+=1





# N = int(input())
# front  = list()
# back = list()

# mid = int(input())
# idx1 = 0
# idx2 = 0
# for i in range(N-1):
#     tmp = int(input())
#     if i == 0:
#         if tmp < mid :
#             front.append(tmp)
#             back.append(mid)
#             mid = tmp
#             idx1 += 1
#             idx2 += 1
#             continue
#         else :
#             front.append(mid)
#             back.append(tmp)
#             idx1 += 1
#             idx2 += 1
#             continue
#     if tmp > mid :




N, K = map(int, input().split())  #최대한 큰 금액을 최대한 많이 우겨넣는게 동전 수를 줄이는 방법, 그리디로 풀기
L = list()
for i in range(N):
    L.append(int(input()))

result = 0 #최종 동전 갯수

for i in range(N-1,-1,-1):
    if K <=0 :
        break
    count = K//L[i] #현재 가격의 돈은 몇개나 들어가야 하나
    K -= L[i]*count
    result += count
    # if K <=0 :
    #     break  여기 있어야지 한번 덜 돔

print(result)




#시간 초과 남
# N, K = map(int, input().split())
# L = list()     
# for i in range(N):
#     L.append(int(input()))

# result = 0 #최종 동전 갯수
# tmp = K #현재 단계의 돈

# for i in range(N-1,-1,-1):
#     if tmp <=0 :
#         break
#     count = 0 #현재 가격의 돈은 몇개나 들어가야 하나
#     while True:
#         if tmp-L[i] < 0 :
#             break
#         else:
#             tmp -= L[i]
#             count += 1
#     if count == 0 :
#         continue
#     result += count

# print(result)
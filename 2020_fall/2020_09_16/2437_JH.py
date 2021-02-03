N = int(input())  #이걸 어떻게 생각해내,,,
L = list(map(int,input().split()))
L.sort() #L을 오름차순으로 정렬
tmp = 1
for i in range(N):
    if tmp < L[i]:
        break
    tmp += L[i]
print(tmp)




# import sys
# sys.setrecursionlimit(2000)
# def solve(L,i,j,tmp):
#     if j == len(L) or tmp+L[j] > i: #L의 가장 무거운 무게까지 탐색 했는데도 목표 무게를 만들 수 없다면 False임. 이전 index까진 무게가 부족했었음. 그 다음 큰 값을 넣었더니 무게가 넘어버리면 현재 재귀해봤자 의미 없다.
#         return False
#     ret = False
#     tmp += L[j]
#     if tmp == i : #해당 추를 올렸더니 무게를 맞추게 되면 True
#         return True
#     for k in range(j,len(L)):
#         ret = solve(L,i,k+1,tmp)
#         if ret : #해당 무게를 만들 수 있게 되면 무조건 True 리턴
#             return True
#     return ret
    

# N = int(input())
# L = list(map(int,input().split()))
# L.sort() #L을 오름차순으로 정렬

# if L[0] != 1 : #만약 L에 1이 없다면 나타낼 수 없는 무게의 최솟값은 1이 될거임
#     print(L[0]-1)
#     exit(0)
# else :
#     for i in range(2,1000000001): #추로 나타낼 수 있는 무게의 범위는 2부터 1 000 000 000
#         result = False
#         for j in range(len(L)):  #L은 오름차순으로 되어있기 때문에 처음 시작하는 무게가 정해지면 뒤에 무게를 돌아볼 필요 없음
#             result = solve(L,i,j,0) #i는 현재 탐색하고 있는 무게, j는 L의 시작 index
#             if result : #해당 무게를 표현 할 수 있다면 주체 말고 stop
#                 break
#         if result == False : #해당 무게를 만들 수 없다면 print 하고 바로 종료
#             print(i)
#             exit(0)



# # N = int(input())    #메모리 초과 ㅠ, 1182는 됐는데 ㅠ
# # L = list(map(int,input().split()))
# # tmp = []

# # for i in range(len(L)):
# #     tmp.append(L[i])
# #     for j in range(len(tmp)-2,-1,-1):
# #         tmp.append(L[i]+tmp[j])
# # tmp.sort()
# # for i in range(1,len(tmp),1):
# #     if tmp[i-1]+1 != tmp[i] :
# #         if tmp[i-1] == tmp[i] :
# #             continue
# #         else :
# #             print(tmp[i-1]+1)
# #             exit(0)
# # print(tmp[-1]+1)
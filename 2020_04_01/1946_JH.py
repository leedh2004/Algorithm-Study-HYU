T = int(input())  #python3는 시간초과, pypy3는 정답, 리스트 한번 쭉 읽기는 해야 할 거 같음 -> 여기서 더 최적화 할 수 있나 ?

for i in range(T):
    N = int(input())
    C = [True]*(N)
    L = list()
    for j in range(N): #순위 리스트 만들어 주기
        a,b = map(int,input().split())
        L.append((a,b))
    L = sorted(L,key=lambda L : L[0])
    m = L[0][1]  
    for k in range(1,N,1): #이제 면접 점수가 위에 친구들보다 크면 무조건 떨어지는거임, 리스트 한번만 읽으면 됨
        if L[k][1] > m :
            C[k] = False
        else :
            m = L[k][1]
    print(C.count(True))




# T = int(input())  #시간초과

# for i in range(T):
#     N = int(input())
#     C = [True]*(N)
#     L = list()
#     for j in range(N): #순위 리스트 만들어 주기
#         a,b = map(int,input().split())
#         L.append((a,b))
#     L = sorted(L,key=lambda L : L[0])
#     m = L[0][1]  
#     for k in range(1,N,1): #이제 면접 점수가 위에 친구들보다 크면 무조건 떨어지는거임, 리스트 한번만 읽으면 됨
#         if L[k][1] > m :
#             C[k] = False
#         else :
#             m = L[k][1]
#     print(C.count(True))



# T = int(input())   #시간초과 뜸

# for i in range(T):
#     N = int(input())
#     C = [True]*(N)
#     L = list()
#     for j in range(N): #순위 리스트 만들어 주기
#         a,b = map(int,input().split())
#         L.append((a,b))
#     L = sorted(L,key=lambda L : L[0]) #서류 순위로 오름차순 정렬
#     for k in range(1,N,1): #한명 한명씩 모두 조사 할거임
#         for l in range(k-1,-1,-1): #위로 올라가면서 나보다 면접 잘본 애 있으면 걔는 합격 못함
#             if L[k][1] > L[l][1] :
#                 C[k] = False
#                 break
#     print(C.count(True))


# T = int(input())  #시간초과 뜸

# for i in range(T):
#     N = int(input())
#     C = [True]*(N)
#     L = list()
#     for j in range(N): #순위 리스트 만들어 주기
#         a,b = map(int,input().split())
#         L.append((a,b))
#     for k in range(N): #한명 한명씩 모두 조사 할거임
#         for l in range(N): #k로 한명 정해지면 이제 나머지 인원들 살피며 합격할 수 있나 조사
#             if L[l][0] < L[k][0] and L[l][1] < L[k][1] :
#                 C[k]= False
#     print(C.count(True))
N,M,K = map(int,input().split())  #시간초과 뜰 줄 알았는데 되넹

for i in range(K,0,-1):
    first = min(((N-1)//2),(M//1))  #여자에서 뺄건지
    second = min((N//2),((M-1)//1)) #남자에서 뺄건지
    if first > second:
        N -= 1
    else :
        M -= 1
print(min(N//2,M//1))

# while True:  #while 이용해서 짠 거
#     if K==0:
#         break
#     first = min(((N-1)//2),(M//1))
#     second = min((N//2),((M-1)//1))
#     if first > second:
#         N -= 1
#     else :
#         M -= 1
#     K -= 1 
# print(min(N//2,M//1))
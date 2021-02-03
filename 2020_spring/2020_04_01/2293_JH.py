n, k = map(int,input().split())  
c = list()
mat = [0]*(k+1)  #0번째 인덱스를 사용하기 위함(아래 설명), k를 mat에서 k로 접근하기 위해(편의 상)
mat[0] = 1 #이걸 지정해주지 않는다면 mat[초기에 들어온 동전값]을 1로 초기화 해주면 됨, 되는데 아래 for문 돌때 매끄럽지 않게 코드를 짜야함
for i in range(n):
    c.append(int(input()))

def dp(k):
    global c
    for i in c :
        for j in range(1,k+1,1):
            if j-i>=0: #0이 포함되어야 하는 이유는 처음 들어온 동전들은 그 동전 한개 써서 만들 수 있음, +1 해줘야함
                mat[j] += mat[j-i]

dp(k)
print(mat[k])


# n, k = map(int,input().split())  #숫자의 합을 만드는 순서가 같아도 다른 걸로 인정되면 이 코드로
# c = list()
# mat = [0]*(k+1)
# for i in range(n):
#     a = int(input())
#     c.append(a)
#     mat[a] = 1

# def dp(k):
#     global n
#     for i in range(n):
#         if k-c[i]>0:
#             mat[k] += mat[k-c[i]]

# for i in range(1,k+1,1):
#     dp(i)
# print(mat[k])
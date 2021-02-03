N = int(input())
L = [int(input()) for _ in range(N)]
L = sorted(L,reverse=True)
V = list()
for i in range(N):
    V.append(L[i]*(i+1))
print(max(V))

# for i in range(len(L)): # 5 4 2 2 2 가 반례임
#     if (L[i]*(i+1)) < tmp:
#         break
#     tmp = L[i]*(i+1)
# print(tmp)
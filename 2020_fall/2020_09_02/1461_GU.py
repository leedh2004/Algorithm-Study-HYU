import sys

N,M = map(int,sys.stdin.readline().split())
books = list(map(int,sys.stdin.readline().split()))
books.append(0)
books.sort()
# 0 넣어서 음수 몇개인지, 양수 몇개인지 확인
left = books.index(0)
right = N - left
books.remove(0)
res = []

#음수 값들은 절대값으로 넣어줌
for i in range(0,left,M):
    res.append(abs(books[i]))
for i in range(N-1,left-1,-M):
    res.append(books[i])
#print(res)
#for i in range(len(res)):
#    res[i] = abs(res[i])
# 두번 왕복
ans = 2 * sum(res)
# 그러나 마지막에 제일 큰 것 갈 때는 안돌아와도 됨
ans -= max(res)
print(ans)

    
import sys
input = sys.stdin.readline

N = int(input())
people = dict()

for i in range(N):
    people[i] = int(input())-1

result = -1
count = -1

for i in people:
    visit = [False for _ in range(N)]
    visit[i] = True
    next_key = people[i]
    tmp_count = 0
    while True :
        if visit[next_key] == True:
            if tmp_count > count :
                result = i
                count = tmp_count
            break
        # 파이썬 3.7부터 딕셔너리의 key 순서는 삽입 순서를 보존하기 때문에 위의 if문 1개로 처리 가능하다.
        # 단 딕셔너리를 비교할때는 삽입순서가 다르더라도 두 딕셔너리가 같으면 같은 딕셔너리로 판단한다. (다르게 판단하려면 collections의 ordered dict 사용)
            # if tmp_count == count :
            #     result = min(result, i)
            #     count = tmp_count
            #     break

        visit[next_key] = True
        next_key = people[next_key]
        tmp_count += 1

print(result+1)
        


# a = {1:2,2:3}
# b = {1:3,2:2}
# c = {2:2,3:3}
# d = {2:3,1:2}
# print(a==b)
# print(a==c)
# print(a==d)


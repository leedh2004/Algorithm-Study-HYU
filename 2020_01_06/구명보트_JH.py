#효율성 테스트 1만 실패함
# people = [70, 50, 80, 50]
people = [70, 50, 80]
limit = 100
result = 0
people.sort()
while people:
    if  people[-1] + people[0] <= limit :
        people.pop(0)
        if people :
            people.pop(-1)
    else :
        people.pop(-1)
    result += 1
print(result)


#효율성에서 실패함
# people = [70, 50, 80, 50]
# people = [70, 50, 80]
# limit = 100
# result = 0
# while people :
#     tmp2 = min(people)
#     tmp = people.pop(people.index(max(people)))
#     if tmp+tmp2 <= limit :
#         if people :
#             tmp2 = people.pop(people.index(tmp2))
#     result += 1
# print(result)
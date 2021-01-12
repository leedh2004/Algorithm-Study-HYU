def solution(people, limit):
    answer = 0
    # 40 <=사람 무게 <=240 and 40 <=구명보트 <=240
    people.sort(reverse = True)
    while len(people) > 0:
        boat = people.pop(0)
        while len(people) > 0:
            light = people[-1]
            if light + boat <= limit:
                boat += light
                people.pop()
            else: break
        answer += 1

    return answer

people = list(map(int,input().split()))
limit = int(input())
print(solution(people,limit))
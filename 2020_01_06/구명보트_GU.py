
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    while len(people) > 0:
        boat = people.pop(0)
        print("first while",boat)
        while len(people) > 0:
            light = people[-1]
            if light + boat <= limit:
                boat += light
                people.pop()
            else: 
                break
            print("seconde while",boat)
        answer += 1

    return answer

people = list(map(int,input().split()))
limit = int(input())
print(solution(people,limit))
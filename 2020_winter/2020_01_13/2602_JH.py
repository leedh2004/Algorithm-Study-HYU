#22퍼에서 시간초과 뜹니당 ㅠ

magic = list(input())
devil = list(input())
angel = list(input())
result = 0
L = len(magic)

def solution(idx, next_list, now_list):
    global magic, result, L
    if idx == L:
        result += 1
        return
    
    for i, c in enumerate(next_list):
        if(c == magic[idx]):
            solution(idx+1, now_list[i+1:], next_list[i+1:])

for i in range(0, len(devil), 1):
    if devil[i] == magic[0] :
        solution(1, angel[i+1:], devil[i+1:])
        # print(i)
    if angel[i] == magic[0] :
        solution(1, devil[i+1:], angel[i+1:])
        # print(i)

print(result)
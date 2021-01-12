#왜 틀렸을까요 ?

magic = list(input())
devil = list(input())
angel = list(input())
result = 0
L = len(magic)

def solution(now_c, idx, next_list, now_list):
    global magic, result, L
    if idx == L:
        if now_c == magic[-1]:
            result += 1
        return
    
    for i, c in enumerate(next_list):
        if(c == magic[idx]):
            solution(c, idx+1, now_list[i+1:], next_list[i+1:])

for i in range(0, len(devil), 1):
    if devil[i] == magic[0] :
        solution(magic[0], 1, angel[i+1:], devil[i+1:])
        print(i)
    if angel[i] == magic[0] :
        solution(magic[0], 1, devil[i+1:], angel[i+1:])
        print(i)

print(result)
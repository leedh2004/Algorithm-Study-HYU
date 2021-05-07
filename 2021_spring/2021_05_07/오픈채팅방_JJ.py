def solution(record):
    nameTable = {}
    answer = []
    for each in record:
        data = each.split()
        if data[0] == 'Enter' or data[0] == 'Change':
            nameTable[data[1]] = data[2]
        
    for each in record:
        data = each.split()
        if data[0] == 'Enter':
            answer.append(nameTable[data[1]]+'님이 들어왔습니다.')
        elif data[0] == 'Leave':
            answer.append(nameTable[data[1]]+'님이 나갔습니다.')
            
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
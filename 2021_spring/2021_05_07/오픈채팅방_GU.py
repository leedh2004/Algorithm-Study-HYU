def solution(record):
    answer = []
    d = dict()
    for i in range(len(record)):
        record[i] = list(record[i].split())
        if record[i][0] == 'Enter' or record[i][0] == 'Change':
            d[record[i][1]] = record[i][2]
    for i in range(len(record)):
        if record[i][0] == 'Change':
            continue
        if record[i][0] == 'Enter':
            answer.append(d[record[i][1]] + "님이 들어왔습니다.")
        else:
            answer.append(d[record[i][1]] + "님이 나갔습니다.")
    return answer

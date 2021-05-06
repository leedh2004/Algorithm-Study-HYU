from collections import defaultdict
def solution(record):
    answer = []
    d = defaultdict()
    for r in record:
        r = r.split()
        if r[0] == 'Enter' or r[0] == 'Change':
            d[r[1]] = r[2]
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer.append(d[r[1]] + "님이 들어왔습니다.")
        elif r[0] == 'Leave':
            answer.append(d[r[1]] + "님이 나갔습니다.")
    return answer
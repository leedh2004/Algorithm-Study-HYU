from collections import defaultdict

def solution(record):
    answer = []
    last_nick = defaultdict(str)
    
    for r in record :
        records = r.split()
        try :
            last_nick[records[1]] = records[2]
        except IndexError :
            continue


    for r in record :
        records = r.split()
        if records[0] == "Enter" :
            answer.append("".join( last_nick[records[1]]+"님이 들어왔습니다."  ))  
        elif records[0] == "Leave" :
            answer.append("".join( last_nick[records[1]]+"님이 나갔습니다."  ))  
        else :
            continue
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
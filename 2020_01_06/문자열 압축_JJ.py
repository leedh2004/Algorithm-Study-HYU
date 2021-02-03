def cut(s,num):
    idx = 0
    tmp = []
    while idx < len(s):
        if idx+num < len(s) :
            tmp.append(s[idx:idx+num])
        else :
            tmp.append(s[idx:])
        idx = idx + num
    return tmp

def solution(s):
    
    # 초기값
    answer = len(s)
    
    # i는 자를 사이즈 
    for i in range(1,int(len(s)/2)+1):
        tmp_answer = len(s)
        parsed = cut(s,i) 
    
        flag = 0
        for j in range(1,len(parsed)):
            
            if parsed[j] == parsed[j-1]:
                # 앞에 이미 숫자를 쓴 경우
                if flag > 1:
                    
                    flag = flag + 1
                    
                    string = str(flag)
                    sub_string = string[1:]
                    
                    # 앞자리 1이고, 뒤에가 0000 꼴일 때
                    if string[0]=='1' and len(sub_string) > 0 and int(sub_string)==0:
                        tmp_answer = tmp_answer - i + 1
                    else : 
                        tmp_answer = tmp_answer - i
                    
                # 숫자를 안 쓴 경우    
                else:
                    flag = 2
                    tmp_answer = tmp_answer - i + 1

            else :
                flag = 1
        answer = min(answer,tmp_answer)
    return answer
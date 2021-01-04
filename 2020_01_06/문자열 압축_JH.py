def solution(s):
    result = dict()
    for i in range(1, len(s)+1, 1):
        
        sub_strings = list()    
        for j in range(0, (len(s))-i+1, i ):   #1개씩 잘랐을때, 2개씩 잘랐을때...... 
            sub_strings.append(''.join(s[j:j+i]))
            if( len(s)-(j+i) != 0 and (len(s)-(j+i)) < i  ) :
                sub_strings.append(''.join(s[j+i:]))
                break
        # print(sub_strings)
        

        tmp_result = ''  #자른 애들 비교
        first = sub_strings[0]
        count_sub = 1
        for j in range(1, len(sub_strings)):
            if first == sub_strings[j] :
                count_sub += 1
            else :
                if count_sub == 1 :
                    tmp_result += first
                    first = sub_strings[j]
                else :
                    tmp_result += str(count_sub) + first
                    count_sub = 1
                    first = sub_strings[j]
        if count_sub == 1 :  #마지막 조사한거 넣어주기
            tmp_result += first
        else :
            tmp_result += str(count_sub)+first

        result[tmp_result] = len(tmp_result)
    # print(result)
    answer = min(result.values())

    return answer

print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
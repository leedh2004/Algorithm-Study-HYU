def solution(s):
    answer = len(s)

    length = answer // 2

    while length > 1:
        tmp_ans = len(s)
        c_start = 0
        c_end = length
        n_start = length
        n_end = 2*length
        cur = s[c_start:c_end]
        next_chunk = s[n_start:n_end]

        cnt = 0
        while True:
            if cur == next_chunk:
                cnt += 1

                # 같은 길이 자르기로 계속 진행(cur 안바꿈)
                if n_end + length <= len(s):
                    n_start += length
                    n_end += length
                    next_chunk = s[n_start:n_end]
                    continue
            # 같은 길이 자르기로 계속 진행(cur 바꿈)
            if n_end + length <= len(s):
                if cnt > 0:
                    tmp_ans -= cnt * length
                    if cnt >= 9:
                        if cnt < 99: # 10 이상 100 미만(두자리수)
                            tmp_ans += 2
                        else: # 100 이상(세자리수)
                            tmp_ans += 3
                    else: # 10 미만(한자리 수)
                        tmp_ans += 1
                
                    cnt = 0
                c_start = n_start
                c_end = n_end
                n_start = c_end
                n_end = n_start + length
                cur = s[c_start:c_end]
                next_chunk = s[n_start:n_end]
            # length 1 줄이고 다시 진행
            else:
                if cnt > 0:
                    tmp_ans -= cnt * length
                    if cnt >= 9: # 10이 아닌 9!!!! 
                        if cnt < 99: # 10 이상 100 미만(두자리수)
                            tmp_ans += 2
                        else: # 100 이상(세자리수)
                            tmp_ans += 3
                    else: # 10 미만(한자리 수)
                        tmp_ans += 1
                
                    cnt = 0
                answer = min(answer,tmp_ans)
                length -= 1
                break
    #print("mid answer",answer)

    # 한글자 단위로 개수 분석
    # 길이 1,2인 경우 줄일 수 없다.
    if len(s) > 2:
        tmp_ans = len(s)
        i = 0
        while i < len(s):
            cur = s[i]
            cnt = 0
            while True:
                if i+1 < len(s):
                    if cur == s[i+1]:
                        cnt += 1
                        i += 1
                    else: break
                else: break
            if cnt > 0:
                tmp_ans -= cnt
                if cnt >= 9:
                    if cnt < 99: # 10 이상 100 미만(두자리수)
                        tmp_ans += 2
                    else: # 100 이상(세자리수)
                        tmp_ans += 3
                else: # 10 미만(한자리 수)
                    tmp_ans += 1
            
                cnt = 0
            i += 1
        answer = min(answer,tmp_ans)
            
                
    return answer

s = input()
print(solution(s))
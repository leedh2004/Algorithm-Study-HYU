def solution(number, k):
    
    # 그리디
    # 문자열을 왼쪽에서 순회하면서, 큰수를 뽑음
    
    ans_list = []
    count = 0
    
    for i in range(len(number)):
        for j in range(len(ans_list)-1,-1,-1):

            # 기존 숫자보다 더 큰게 나타났을 때
            if ans_list[j] < number[i] and count < k:
                ans_list.pop()
                count = count + 1
            else :
                break
            
        # 뒤에 숫자가 남아있을때 붙여주기
        if count == k:
            ans_list = ans_list + list(number)[k+len(ans_list):]
            break
        
        ans_list.append(number[i])
        
    return "".join(ans_list[:len(number)-k])
def solution(people, limit):
    
    # 1인 1보트로 가정
    count = len(people)
    
    # 오름차순으로 정렬
    people.sort()
    
    first_idx = 0
    
    for i in range(len(people)-1,-1,-1):
        
        if first_idx<i and people[first_idx] + people[i] <= limit:
            count = count - 1
            first_idx = first_idx + 1
            
    return count
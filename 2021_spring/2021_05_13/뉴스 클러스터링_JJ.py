from collections import defaultdict

def solution(str1, str2):
    dict1 = makeDict(str1)
    dict2 = makeDict(str2)
    # print(dict1)
    # print(dict2)
    answer = int(getZacard(dict1,dict2)*65536)
    return answer

def makeDict(str1):
    ret = defaultdict(int)
    for i in range(0,len(str1)-1):
        st = str1[i:i+2]
        if st.isalpha():
            upperSt = st.upper()
            ret[upperSt] = ret[upperSt] + 1
    return ret

def getZacard(dict1,dict2):
    keword = set(dict1.keys()) | set(dict2.keys())
    inner = 0
    outer = 0 
    for k in keword:
        inner = inner + min(dict1[k],dict2[k])
        outer = outer + max(dict1[k],dict2[k])
    if outer == 0:
        return 1
    elif inner == 0:
        return 0
    else :
        return inner/outer
        
solution('FRANCE','french')
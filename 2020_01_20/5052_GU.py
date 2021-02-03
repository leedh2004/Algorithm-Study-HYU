import sys
# 트라이 알고리즘
class Node():
    def __init__(self,key,last=False):
        self.key = key
        self.last = last
        # dict
        self.children = {}

class Trie():
    def __init__(self):
        self.root =Node(None)

    def insert(self,string):
        cur = self.root

        for char in string:
            if char == '\n':
                cur.last = True
            else:
                if char not in cur.children:
                    cur.children[char] = Node(char)
                cur = cur.children[char]
                if cur.last:
                    return False
                
        return True

    # def search(self,string):
    #     cur = self.root

    #     for char in string:
    #         if char in cur.children:
    #             cur = cur.children[char]
    #         else:
    #             return False

    #     if cur.last == True:
    #         return True
    #     else:
    #         return False

        


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    T = Trie()
    flag = True
    phone_num = []
    for j in range(n):
        phone_num.append(sys.stdin.readline())
    # sort 안하면 틀린다!!!!!!!!
    phone_num.sort(key=len)
    for j in range(n):
        if not flag:
            break
        if not T.insert(phone_num[j]):
            flag = False
    if flag: print("YES")
    else: print("NO")

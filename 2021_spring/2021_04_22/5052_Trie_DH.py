import sys
from collections import defaultdict
T = int(sys.stdin.readline().strip())

class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True
    
    def search(self, word):
        cur = self.head
        for ch in word:
            if '*' in cur.child:
                return True
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        if '*' in cur.child:
            return True
        return False

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    t = Trie()
    flag = True
    
    test_set = []
    for _ in range(N):
        s = sys.stdin.readline().strip()
        if t.search(s):
            flag = False
        t.insert(s)
    if flag:
        print("YES")
    else:
        print("NO")

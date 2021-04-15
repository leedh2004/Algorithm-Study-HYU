import sys


class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head

        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
            cur = cur.children[char]

        cur.data = string

    def search(self, string):
        cur = self.head

        for char in string:
            if char not in cur.children:
                return False
            cur = cur.children[char]

        if cur.data == string:
            return True
        else:
            return False


N, M = map(int, sys.stdin.readline().split())
T = Trie()
for _ in range(N):
    T.insert(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(M):
    if T.search(sys.stdin.readline().rstrip()):
        cnt += 1
print(cnt)

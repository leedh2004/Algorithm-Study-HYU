import sys


class Node():
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.child_node = {}


class Trie():
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        cur_node = self.head

        for chr in string:
            # 노드 순차적 검색하며 없으면 노드등록
            if chr not in cur_node.child_node.keys():
                cur_node.child_node[chr] = Node(chr)

            # 현재노드를 다음 문자의 노드로 변경
            cur_node = cur_node.child_node[chr]

            # 만약 옮겨간 노드에서 이미 데이터를 가지고 있다면 이미 짧은 녀석을 등록한 거임
            if cur_node.data:
                return False

        # 마지막 노드에는 문자열 전체 저장
        cur_node.data = string

        # 마지막 노드에 저장했는데 자식이 있는 경우
        # 이미 중복되는 더 긴 녀석을 등록했던 거임
        if bool(cur_node.child_node):
            return False

        return True


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    flag = True
    trie = Trie()
    for j in range(n):
        phoneNumber = sys.stdin.readline().rstrip()
        if flag:
            flag = trie.insert(phoneNumber)
    if flag:
        print("YES")
    else:
        print("NO")

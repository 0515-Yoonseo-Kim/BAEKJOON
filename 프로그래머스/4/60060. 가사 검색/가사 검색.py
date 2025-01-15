class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.cnt = 0  # 해당 노드를 지나가는 단어 수 저장
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        # 각 노드를 지날 때마다 cnt 증가
        for w in word:
            if w not in node.children:
                node.children[w] = Node()
            node = node.children[w]
            node.cnt += 1
        node.is_end = True
        
    def search(self, query):
        node = self.root
        
        if all(q == '?' for q in query):
            return sum(child.cnt for child in node.children.values())
        
        for q in query:
            if q == "?":
                return node.cnt  # ? 이후의 단어 수 반환
            if q not in node.children:
                return 0  # 해당 경로가 없을 경우
            node = node.children[q]
        return node.cnt if node.is_end else 0


def solution(words, queries):
    answer = []
    tries = {}
    reversed_tries = {}
    
    # ✅ 단어를 길이별로 나누어 정방향 & 역방향 트라이에 삽입
    for word in words:
        length = len(word)
        if length not in tries:
            tries[length] = Trie()
            reversed_tries[length] = Trie()
            
        # 단어를 정방향 & 역방향으로 추가
        tries[length].insert(word)
        reversed_tries[length].insert(word[::-1])
    
    # ✅ 쿼리 처리
    for query in queries:
        length = len(query)
        # 해당 길이의 트라이가 없을 경우
        if length not in tries:
            answer.append(0)
            continue
        
        
        
        # ✅ 접두사 검색
        if query[0] != '?':
            trie = tries[length]
            answer.append(trie.search(query))
        # ✅ 접미사 검색 (역방향)
        else:
            trie = reversed_tries[length]
            answer.append(trie.search(query[::-1]))
    
    return answer
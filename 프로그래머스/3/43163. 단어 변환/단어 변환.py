# 조건에 맞으면 visited 체크 아니면 pass
# 도착하기 전 아무것도 변환할 수 없는 경우에 0
# cnt도 같이 셈
from collections import deque
def can_convert(w1,w2):
    chk = False
    for i in range(len(w1)):
        if w1[i]!=w2[i]:
            if chk == True:
                return False
            else:
                chk = True
    return True
def solution(begin, target, words):
    visited = {k:False for k in words}
    visited[begin]=False
    queue = deque([(begin,0)])
    while queue:
        curr_word, curr_cnt = queue.popleft()
        if curr_word == target:
            return curr_cnt
        if visited[curr_word]:
            continue
        visited[curr_word]=True
        for word in words:
            if can_convert(curr_word,word):
                queue.append([word,curr_cnt+1])
            else:
                continue
        
    answer = 0
    return answer
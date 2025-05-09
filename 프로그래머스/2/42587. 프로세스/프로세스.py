# queue에 들어간 것을 빼면서
# 남은 queue의 값을 탐색
# 도중에 우선순위가 더 큰 것이 나오면 다시 append
# 만약에 실행될 순서이면 cnt높이고 궁금한 프로세스면 바로 return 
from collections import deque
def solution(priorities, location):
    queue = deque([[idx,p] for idx, p in enumerate(priorities)])
    cnt = 0
    while queue:
        curr_idx, curr_p = queue.popleft()
        if any(curr_p < p for _,p in queue):
            queue.append([curr_idx,curr_p])
        else:
            cnt += 1
            if curr_idx == location:
                return cnt
    return cnt
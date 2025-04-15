import math
from collections import deque
def solution(progresses, speeds):
    days = [0]*len(speeds)
    for idx, (p, s) in enumerate(zip(progresses, speeds)):
        days[idx] = math.ceil((100-p)/s)
    queue = deque(days)
    answer = []
    curr_days = queue.popleft()
    cnt = 1
    while queue:
        now = queue.popleft()
        if curr_days >= now:
            cnt += 1
        else:
            curr_days = now
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer
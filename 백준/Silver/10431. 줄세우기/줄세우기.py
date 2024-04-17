import sys
from collections import deque
import heapq
input = sys.stdin.readline

T = int(input())

for testcase in range(1,T+1):
    lines = deque(list(map(int,input().split()[1:])))
    indicator = lines.popleft()
    new_lines = [indicator]
    cnt = 0
    while lines:
        now = lines.popleft()
        for i in range(len(new_lines)):
            if new_lines[-i] > now:
                cnt+=1
        heapq.heappush(new_lines,now)

    print(testcase,cnt)

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

def command(line,queue):
    line = list(line.split())
    if line[0]=="push":
        queue.append(line[1])
    elif line[0]=="pop":
        if queue:
            now = queue.popleft()
            print(now)
        else:
            print(-1)
    elif line[0]=="size":
        print(len(queue))
    elif line[0]=="empty":
        if queue:
            print(0)
        else:
            print(1)
    elif line[0]=="front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif line[0]=="back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    return queue

queue = deque()
for _ in range(N):
    queue = command(input(),queue)

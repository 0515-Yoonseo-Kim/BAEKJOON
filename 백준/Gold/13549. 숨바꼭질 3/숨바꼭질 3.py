from collections import deque
MAX = 100001
check = [False] * (2*MAX)
dist = [-1] * (2*MAX)

start,end = map(int, input().split())
queue = deque()
queue.append(start)
check[start] = True
dist[start] = 0

while queue:
    now = queue.popleft()
    if now*2 <= MAX and check[now*2] == False:
        queue.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]

    if now - 1 >= 0 and check[now-1] == False:
        queue.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] + 1

    if now + 1 <= MAX and check[now+1] == False:
        queue.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now] + 1

print(dist[end])
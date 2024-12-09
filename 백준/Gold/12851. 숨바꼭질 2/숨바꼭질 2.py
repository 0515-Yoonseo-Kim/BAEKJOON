from collections import deque

N, M = map(int,input().split())
visited = [0]*100001
queue = deque([N])
cnt = 0

while queue:
    now = queue.popleft()
    if now == M:
        cnt += 1
        continue

    for new in [now-1,now+1,2*now]:
        if 0<=new<100001:
            if visited[new] == 0:
                visited[new] += visited[now] + 1
                queue.append(new)
            else:
                if visited[new] == visited[now] + 1:
                    queue.append(new)
print(visited[M])
print(cnt)
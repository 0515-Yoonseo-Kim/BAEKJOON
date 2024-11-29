import sys
import heapq

input = sys.stdin.readline

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append([b,t])

INF = int(1e9)

# 다익스트라 알고리즘
def dijkstra(st):
    dist = [INF] * (N + 1)
    hq = []
    heapq.heappush(hq, (0, st))
    dist[st] = 0

    while hq:
        current_dist, now = heapq.heappop(hq)

        if current_dist > dist[now]:
            continue

        for neighbor, weight in graph[now]:
            cost = current_dist + weight
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(hq, (cost, neighbor))

    return dist

to_x = [dijkstra(i)[X] for i in range(1, N + 1)]

from_x = dijkstra(X)[1:]

max_time = 0
for t,f in zip(to_x,from_x):
    max_time = max(max_time,t+f)
print(max_time)
    
import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

INF = int(1e9)

def dijkstra(start):
    hq = []
    dist = [INF] * (N + 1)
    heapq.heappush(hq, (0, start))
    dist[start] = 0

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

# 특정 경유지 입력
n1, n2 = map(int, input().split())

# 다익스트라 결과 저장
dist_from_1 = dijkstra(1)
dist_from_n1 = dijkstra(n1)
dist_from_n2 = dijkstra(n2)

# 두 가지 경로의 거리 계산
path1 = dist_from_1[n1] + dist_from_n1[n2] + dist_from_n2[N]
path2 = dist_from_1[n2] + dist_from_n2[n1] + dist_from_n1[N]

# 불가능한 경로 처리
result = min(path1, path2)
print(result if result < INF else -1)

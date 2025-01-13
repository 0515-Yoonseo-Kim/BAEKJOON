N, M = map(int, input().split())
edges = []
INF = int(1e8)
distance = [INF] * (N + 1)

# 음의 가중치 존재 -> 다익스트라(X) 벨만-포드(O)
for _ in range(M):
    edge = list(map(int, input().split()))
    edges.append(edge)

def bellman_ford(start):
    distance[start] = 0

    for _ in range(N - 1):
        for a, b, c in edges:
            if distance[a] != INF and distance[a] + c < distance[b]:
                distance[b] = distance[a] + c

    for a, b, c in edges:
        if distance[a] != INF and distance[a] + c < distance[b]:
            print(-1)  # 음의 사이클 존재 시 -1만 출력
            return

    print("\n".join(map(str, [d if d != INF else -1 for d in distance[2:]])))

bellman_ford(1)

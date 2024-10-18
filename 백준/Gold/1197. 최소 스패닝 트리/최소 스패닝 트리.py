import heapq
from collections import defaultdict

V,E = map(int,input().split())
graph = defaultdict(list)

for _ in range(E):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def prim(graph,start) -> None:
    visited = set()

    min_heap = [(0,start)]
    total_weight = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)
        total_weight += weight
        for node, w in graph[u]:
            if node not in visited:
                heapq.heappush(min_heap, (w, node))
    return total_weight

print(prim(graph,1))


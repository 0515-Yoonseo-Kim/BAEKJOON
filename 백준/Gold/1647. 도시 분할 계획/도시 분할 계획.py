import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
# 마을 정보 입력
N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def prim(graph, st):
    visited = [False]*(N+1)
    min_heap = [(0,st)]
    total_weight = 0
    max_weight = 0

    while min_heap:
        weight,node = heapq.heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight
        max_weight = max(max_weight,weight)
        for n,w in graph[node]:
            if not visited[n]:
                heapq.heappush(min_heap,(w,n))
                
    return total_weight - max_weight


print(prim(graph, 1))

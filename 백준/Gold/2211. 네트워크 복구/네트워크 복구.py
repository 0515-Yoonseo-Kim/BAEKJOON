import heapq
import sys
from collections import defaultdict
from typing import List

input = sys.stdin.readline
N,M = map(int,input().split())
graph = {i:defaultdict(int) for i in range(1,N+1)}
INF = int(1e9)
distances = [INF for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
    
def dijkstra(st) -> List[List[int]]:
    q = []
    heapq.heappush(q,(0,st))
    distances[st] = 0
    edges = {}

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        if curr_dist > distances[curr_node]:
            continue
        
        
        for node, dist in graph[curr_node].items():
            new_dist = curr_dist + dist
            if new_dist < distances[node]:
                distances[node] = new_dist
                heapq.heappush(q,(new_dist,node))
                edges[node] = [curr_node, node]

    return list(edges.values())

edges = dijkstra(1)
print(len(edges))
for edge in edges:
    print(*edge)
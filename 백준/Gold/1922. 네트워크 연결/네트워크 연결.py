from collections import defaultdict
import sys
import heapq
from typing import Dict, List, Tuple

input = sys.stdin.readline

def prim(graph: Dict[int, List[Tuple[int, int]]], start: int) -> int:
    queue = [(0, start)]  # (가중치, 노드)
    visited = set()
    total_weight = 0
    
    while queue:
        weight, node = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        total_weight += weight
        
        for w, n in graph[node]:  # w는 가중치, n은 이웃 노드
            if n not in visited:
                heapq.heappush(queue, (w, n))
    
    return total_weight

N = int(input())  # 노드의 수
M = int(input())  # 간선의 수

graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))  # (가중치, 목적지)
    graph[b].append((c, a))  # (가중치, 목적지)

print(prim(graph, 1))

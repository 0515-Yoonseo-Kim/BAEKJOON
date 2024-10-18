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
        
        for n, w in graph[node]:  # (목적지, 가중치) 순서로 그래프에 저장됨
            if n not in visited:
                heapq.heappush(queue, (w, n))  # heapq에 넣을 때 (가중치, 목적지)로 넣음
    
    return total_weight

N = int(input())  # 노드의 수
M = int(input())  # 간선의 수

graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # (목적지, 가중치)로 저장
    graph[b].append((a, c))  # (목적지, 가중치)로 저장

print(prim(graph, 1))

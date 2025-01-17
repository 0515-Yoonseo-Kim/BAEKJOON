from collections import defaultdict
from typing import List
import heapq
import sys

input = sys.stdin.readline

V,M =map(int,input().split())
graph = {k:defaultdict(int) for k in range(1,V+1)}
INF = int(1e8)


for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b], c) if graph[a][b] != 0 else c
    graph[b][a] = min(graph[b][a], c) if graph[b][a] != 0 else c


J,S = map(int,input().split())

def dijkstra(st) -> List[int]:
    distance = [INF for _ in range(V+1)]
    distance[st] = 0
    queue = []
    heapq.heappush(queue,(0,st))

    while queue:
        curr_dist,curr_node = heapq.heappop(queue)
        
        if curr_dist > distance[curr_node]:
            continue

        for next_node in graph[curr_node]:
            next_dist = curr_dist + graph[curr_node][next_node]

            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(queue,(next_dist,next_node))
    
    return distance

def find_locations(distances_list) -> int:
    MAX_DIST = INF*2
    min_dist = MAX_DIST
    locations = []
    for idx, dist in enumerate(distances_list):
        if (idx == J) or (idx == S):
            continue
        
        if sum(dist) == min_dist:
            locations.append(idx)
        elif sum(dist) < min_dist:
            min_dist = sum(dist)
            locations = [idx]

    if min_dist == MAX_DIST:
        return -1

    j_values = [distances_list[loc][0] for loc in locations if distances_list[loc][0] <= distances_list[loc][1]]

    if not j_values:
        return -1

    j_min = min(j_values)
    for loc in locations:
        if distances_list[loc][0] == j_min:
            return loc
    return -1

J_distances = dijkstra(J)
S_distances = dijkstra(S)

print(find_locations(list(zip(J_distances,S_distances))))
from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [defaultdict(int) for _ in range(N+1)]

all_road_weight = 0
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a][b]=c
    graph[b][a]=c
    all_road_weight += c

def prim():
    visited = [False for _ in range(N+1)]
    min_heap = [[0,1]]
    total_weight = 0

    while min_heap:
        w,n = heapq.heappop(min_heap)
        if visited[n]:
            continue
        visited[n] = True
        total_weight += w

        for neighbor,cost in graph[n].items():
            if not visited[neighbor]:
                heapq.heappush(min_heap,[cost,neighbor])

    return total_weight if all(visited[1:]) else -1

total_weight = prim()

if total_weight != -1:
    print(all_road_weight - total_weight)
else:
    print(-1)
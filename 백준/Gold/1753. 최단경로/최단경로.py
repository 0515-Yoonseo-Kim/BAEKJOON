import sys,heapq
from collections import defaultdict
input = sys.stdin.readline

V,E = map(int,input().split())
K = int(input())
INF = 1e9
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

def dijkstra(st):
    min_heap = [(0,st)]
    distance[st] = 0
    while min_heap:
        w,v = heapq.heappop(min_heap)
        if distance[v] < w:
            continue

        for node,weight in graph[v]:
            if distance[v] + weight < distance[node]:
                distance[node] = distance[v] + weight
                heapq.heappush(min_heap,(distance[node],node))

    
dijkstra(K)

for i in range(1,V+1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print("INF")
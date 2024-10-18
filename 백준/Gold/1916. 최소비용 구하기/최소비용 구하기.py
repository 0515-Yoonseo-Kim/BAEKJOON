import sys, heapq
from collections import defaultdict

input = sys.stdin.readline
INF = 1e9

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

start,end = map(int,input().split())

def dijkstra(st,ed):
    min_heap = [(0,st)]
    distance[st] = 0
    while min_heap:
        weight,node = heapq.heappop(min_heap)
        if distance[node] < weight:
            continue

        for n,w in graph[node]:
            if distance[node] + w < distance[n]:
                distance[n] = distance[node] + w
                heapq.heappush(min_heap,(distance[n],n)) 
    return distance[ed]


print(dijkstra(start,end))
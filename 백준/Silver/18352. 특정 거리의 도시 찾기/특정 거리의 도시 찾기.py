import sys
import heapq
input = sys.stdin.readline

#DFS&BFS&다익스트라(우선순위큐)
N,M,K,X = map(int,input().split())
INF = 1e9

#입력단.
node = [0]*(N+1)
road_list = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    node, road = map(int,input().split())
    road_list[node].append(road)

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue,[distance[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distance[current_node] < current_distance:
            continue
        for road in road_list[current_node]:
            if current_distance + 1 < distance[road]:
                distance[road] = current_distance +1    
                heapq.heappush(queue,[distance[road], road])

dijkstra(X)

if K not in distance:
    print(-1)
else:
    for dist in range(len(distance)):
        if distance[dist] == K:
            print(dist)
    

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    indegree[B]+=1


queue = deque()
result = []

for deg in range(1,N+1):
    if indegree[deg] == 0:
        queue.append(deg)

while queue:
    now = queue.popleft()
    result.append(now)
    for sub in graph[now]:
        indegree[sub] -= 1
        if indegree[sub] == 0:
            queue.append(sub)

for re in result:
    print(re,end = " ")



    
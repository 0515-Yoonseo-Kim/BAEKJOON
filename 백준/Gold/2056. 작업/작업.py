import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
indegree = [0]*(N+1)
sub_graph = [[] for _ in range(N+1)]
time_list = [0]*(N+1)
dynamic = [0]*(N+1)
for num in range(1,N+1):
    sub = list(map(int,input().split()))
    T, num_sub = sub[0], sub[1]
    time_list[num] = T
    for i in range(num_sub):
        pre_item = sub[i+2]
        sub_graph[pre_item].append(num) 
        indegree[num] += 1
       
def topology_sorting():
    queue = deque()
    for deg in range(1,N+1):
        if indegree[deg] == 0:
            queue.append(deg)
            dynamic[deg] = time_list[deg]
    while queue:
        now = queue.popleft()
        for sub in sub_graph[now]:
            
            dynamic[sub] = max(dynamic[sub],dynamic[now]+time_list[sub])
            indegree[sub] -= 1
            if indegree[sub] == 0:
                queue.append(sub)
    print(max(dynamic))
    
topology_sorting()
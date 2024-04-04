import sys
from collections import deque

# 입력단
input = sys.stdin.readline

N, M = map(int,input().split())
indegree = [0]*(N+1)
subject_graph = [[] for _ in range(N+1)]

for _ in range(M):
    #A번이 B의 선수 과목
    A,B = map(int,input().split())
    subject_graph[A].append(B)
    indegree[B]+=1
    

#정렬 함수
def topology_sorting():
    result = [0]*(N+1)
    queue = deque()
    for deg in range(1,N+1):
        if indegree[deg] == 0:
            queue.append(deg)
            result[deg] = 1
    
    while queue:
        now = queue.popleft()
        for sub in subject_graph[now]:
            indegree[sub]-=1
            if indegree[sub] == 0:
                queue.append(sub)
                result[sub] = result[now]+1
    
    result = result[1:]
    print(*result)
    

topology_sorting()
        


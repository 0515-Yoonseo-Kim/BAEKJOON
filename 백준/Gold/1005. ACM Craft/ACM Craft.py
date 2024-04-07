# (윤서)
# 첫 번째 시도 : dynamic 테이블 없이 time_list를 그 때 그 때 초기화시킴
# 실패 이유 : 3의 선행 노드 1,2가 있을 시 1,2가 순서대로 들어가는데
# 1보다 2가 빨리 끝나면 queue를 돌면서 빨리 끝난 시간에 다시 초기화 됨
# 해결 : dynamic 테이블로 비교하면서 진행 함.
# 다른 방법으로는 deque 말고 heapq로 시간을 기준으로 정렬시킬 수 있을 것 같다.
import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    indegree = [0]*(N+1)
    sub_graph = [[] for _ in range(N+1)]
    time_list = [0]
    time_list.extend(list(map(int,input().split())))
    dynamic = [0]*(N+1)
    
    for i in range(K):
        A, B = map(int,input().split())
        sub_graph[A].append(B)
        indegree[B] +=1
    goal = int(input())
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
        print(dynamic[goal])

    topology_sorting()
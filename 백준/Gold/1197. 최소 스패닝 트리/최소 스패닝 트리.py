import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
parents = [i for i in range(V+1)]
cost_list = []

# 부모 찾는 함수
def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] = find_parent(parents[x])  # 재귀로 경로 압축 (가장 작은 값을 부모로)
    return parents[x]

# 작은 값을 부모로 합치는 union 함수
def union(x, y):
    parent_x = find_parent(x)
    parent_y = find_parent(y)
    if parent_x > parent_y:
        parents[parent_x] = parent_y
    else:
        parents[parent_y] = parent_x

# 크루스칼 알고리즘
for i in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(cost_list, (C, A, B))  

cost_sum = 0

# 간선을 하나씩 확인하면서
while cost_list:
    cost, a, b = heapq.heappop(cost_list)
    # 사이클이 발생하지 않는 경우에만 선택
    if find_parent(a) != find_parent(b):
        union(a, b)  # 두 노드를 연결
        cost_sum += cost  # 비용을 합산

print(cost_sum)

import sys
import heapq
input = sys.stdin.readline
while True:
    N, M = map(int,input().split())
    if N==0 and M==0:
        break
    total_cost = 0
    cost_list = []
    parents = [i for i in range(N+1)]

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

    for _ in range(M):
        input_string = list(map(int,input().split()))
        if len(input_string) == 3:
            X, Y, distance = input_string
            total_cost += distance
            heapq.heappush(cost_list,(distance,X,Y))
        else:
            break

    cost_sum = 0
    while cost_list:
        cost, a, b = heapq.heappop(cost_list)
        # 사이클이 발생하지 않는 경우에만 선택
        if find_parent(a) != find_parent(b):
            union(a, b)  # 두 노드를 연결
            cost_sum += cost  # 비용을 합산

    print(total_cost-cost_sum)
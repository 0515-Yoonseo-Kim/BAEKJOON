from collections import defaultdict

N, M = map(int, input().split())
friends = defaultdict(list)

# 그래프 입력
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

# 백트래킹 함수
def dfs(node, visited):
    if len(visited) == 5:  # 깊이 5에 도달하면 조건 만족
        return True

    for neighbor in friends[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            if dfs(neighbor,visited):  # 재귀 호출
                return True
            visited.remove(neighbor)  # 백트래킹

    return False

# 전체 탐색
def solution():
    for start in range(N):
        if dfs(start,{start}):
            return 1
    return 0

print(solution())

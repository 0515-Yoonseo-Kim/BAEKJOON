from collections import defaultdict

def solution(info, edges):
    # 그래프 표현
    graph = defaultdict(list)
    for p, c in edges:
        graph[p].append(c)

    def dfs(sheep, wolf, visited):
        # 늑대가 양보다 많아지면 종료
        if wolf >= sheep:
            return 0

        # 현재까지 모은 양의 수가 최대값
        max_sheep = sheep

        # 현재 방문한 모든 노드에서 이동 가능한 노드 탐색
        for node in visited:
            for next_node in graph[node]:
                if next_node not in visited:
                    # 새 노드를 추가한 상태로 탐색
                    new_visited = visited | {next_node}
                    if info[next_node] == 0:  # 양
                        max_sheep = max(max_sheep, dfs(sheep + 1, wolf, new_visited))
                    else:  # 늑대
                        max_sheep = max(max_sheep, dfs(sheep, wolf + 1, new_visited))

        return max_sheep

    # DFS 시작 (0번 노드에서 시작, 양 1마리, 늑대 0마리, 방문 집합에 0 포함)
    return dfs(1, 0, {0})

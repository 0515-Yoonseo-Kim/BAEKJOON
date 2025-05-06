from collections import defaultdict, deque
MAX_VAL = int(1e6)

def reverse_bfs(n, destination, graph):
    visited = [MAX_VAL] * (n + 1)
    visited[destination] = 0
    queue = deque([destination])
    while queue:
        curr_node = queue.popleft()
        for next_node in graph[curr_node]:
            if visited[next_node] > visited[curr_node] + 1:
                visited[next_node] = visited[curr_node] + 1
                queue.append(next_node)
    return visited

def solution(n, roads, sources, destination: int):
    graph = defaultdict(set)
    for st, ed in roads:
        graph[st].add(ed)
        graph[ed].add(st)

    distances = reverse_bfs(n, destination, graph)
    return [distances[src] if distances[src] != MAX_VAL else -1 for src in sources]

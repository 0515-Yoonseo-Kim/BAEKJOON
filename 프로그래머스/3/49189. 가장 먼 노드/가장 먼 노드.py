from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for v in edge:
        st,ed = v
        graph[st].append(ed)
        graph[ed].append(st)
    visited = [-1]*(n+1)
    visited[1]=0
    
    queue = deque([1])
    while queue:
        now = queue.popleft()
        for child in graph[now]:
            if visited[child]==-1:
                visited[child]=visited[now]+1
                queue.append(child)

    return visited.count(max(visited))
def solution(tickets):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for start, end in sorted(tickets):
        graph[start].append(end)
    
    route = []
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop(0))
        route.append(airport)
    
    dfs("ICN")
    return route[::-1]



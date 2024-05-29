def solution(n, wires):
    node = [[] for _ in range(n+1)]
    for wire in wires:
        a,b= wire
        node[a].append(b)
        node[b].append(a)
    # 각 노드 dfs
    visited = [False]*(n+1)
    distance = [[] for _ in range(n+1)]
    def dfs(depth, n):
        visited[n] = True
        for k in node[n]:
            if not visited[k]:
                dfs(depth+1,k)
        distance[n].append(depth)
    dfs(0,1)
    print(distance)
    answer = 100000
    for d in distance:
        for e in d:
            answer = min(abs(n-2*e),answer)
        
        
    return answer
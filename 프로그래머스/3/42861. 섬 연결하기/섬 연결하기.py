import heapq

def solution(n: int, costs: list):
    graph = [[] for _ in range(n+1)]
    connected = [False for _ in range(n+1)]
    

    for cost in costs:
        a,b,c = cost
        graph[a].append([c,b])
        graph[b].append([c,a])

    def prim(st):
        q = []
        total_cost = 0
        heapq.heappush(q,(0,st))
        while q:
            cost, node = heapq.heappop(q)
            if not connected[node]:
                connected[node] = True
                total_cost+=cost

                for i in graph[node]:
                    if not connected[i[1]]:
                        heapq.heappush(q,i)

        return total_cost
    
    return prim(0)

            


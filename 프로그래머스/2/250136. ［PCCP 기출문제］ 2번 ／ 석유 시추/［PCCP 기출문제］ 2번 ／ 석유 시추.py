from collections import deque

# BFS로 하나의 석유 덩어리 찾기
def bfs(arr, visited, N, M, r, c):
    di = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
    cluster = []  # 석유 덩어리의 좌표들을 저장
    queue = deque([(r, c)])
    visited[r][c] = True
    while queue:
        x, y = queue.popleft()
        cluster.append((x, y))  # 덩어리의 좌표 추가
        
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                
    return cluster

def solution(land):
    N, M = len(land), len(land[0])
    visited = [[False] * M for _ in range(N)]
    
    # 석유 덩어리들을 추적
    oil_clusters = []
    
    # 석유 덩어리 찾기
    for r in range(N):
        for c in range(M):
            if land[r][c] == 1 and not visited[r][c]:
                cluster = bfs(land, visited, N, M, r, c)
                oil_clusters.append(cluster)
    
    # 각 열에 대해 얻을 수 있는 석유량 계산
    col_oil = [0] * M  # 각 열에서 얻을 수 있는 석유량을 저장
    
    # 각 덩어리가 어느 열에 걸쳐 있는지 체크
    for cluster in oil_clusters:
        # 해당 덩어리가 포함된 열들을 추적
        cols_in_cluster = set()  # 각 덩어리가 포함된 열을 set에 저장하여 중복을 피함
        for x, y in cluster:
            cols_in_cluster.add(y)
        
        # 해당 덩어리가 포함된 열에 대해서만 석유량 합산
        for col in cols_in_cluster:
            col_oil[col] += len(cluster)
    
    # 가장 많은 석유량을 구함
    return max(col_oil)


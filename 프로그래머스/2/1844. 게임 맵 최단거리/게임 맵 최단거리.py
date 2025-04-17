from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    di = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False]*M for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 1))  # (row, col, count)
    visited[0][0] = True

    while queue:
        r, c, cnt = queue.popleft()
        if (r, c) == (N-1, M-1):
            return cnt
        for dr, dc in di:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, cnt + 1))
    return -1

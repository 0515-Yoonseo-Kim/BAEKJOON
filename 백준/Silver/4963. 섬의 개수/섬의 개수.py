import sys
from collections import deque
input = sys.stdin.readline


def bfs(h, w, arr, visited) -> int:
    if arr[h][w] == 0 or visited[h][w]:
        return 0
    
    W, H = len(arr[0]), len(arr)
    queue = deque([(h, w)])
    visited[h][w] = True

    dr = [-1,0,1,0,1,1,-1,-1]
    dc = [0,1,0,-1,1,-1,1,-1]

    while queue:
        r, c = queue.popleft()
        
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and arr[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = True

    return 1

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(H)]
    visited = [[False for _ in range(W)] for _ in range(H)]
    cnt = 0

    for h in range(H):
        for w in range(W):
            cnt += bfs(h, w, arr, visited)

    print(cnt)

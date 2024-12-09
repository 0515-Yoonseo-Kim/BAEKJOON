import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
max_val = 0

def dfs(visited: set, r: int, c: int) -> None:
    global max_val
    max_val = max(max_val, len(visited))

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in visited:
            visited.add(arr[nr][nc])
            dfs(visited, nr, nc)
            visited.remove(arr[nr][nc])

dfs(set(arr[0][0]), 0, 0)

print(max_val)

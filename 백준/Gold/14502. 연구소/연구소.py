import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
safe_territory = 0
zeros = [(r,c) for r in range(N) for c in range(M) if arr[r][c] == 0]
virus = [(r,c) for r in range(N) for c in range(M) if arr[r][c] == 2]

def bfs(graph):
    queue = deque(virus)
    visited = [[False] * M for _ in range(N)]
    moves = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr,nc = r + moves[i][0], c + moves[i][1]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and graph[nr][nc] == 0:
                visited[nr][nc] = True
                graph[nr][nc] = 2
                queue.append((nr,nc))
    return sum([row.count(0) for row in graph])


for combo in combinations(zeros,3):
    curr_arr = [arr[i][:] for i in range(N)]
    for i in range(3):
        r,c = combo[i]
        curr_arr[r][c] = 1
    safe_territory = max(safe_territory, bfs(curr_arr))


print(safe_territory)
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]    
    while queue:
        x, y = queue.popleft()
        arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if arr[nx][ny] == 1 :
                queue.append((nx,ny))
                arr[nx][ny] = 0


for _ in range(T):
    R, C, K = map(int, input().split())
    global arr
    arr = [[0 for _ in range(C)] for _ in range(R)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)

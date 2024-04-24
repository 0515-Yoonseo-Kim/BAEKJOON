from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = []
goal = []
answer = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    temp = list(map(int,input().split()))
    if 2 in temp:
        goal=[i,temp.index(2)]
    arr.append(temp)

def bfs(li):
    stx,sty = li
    queue = deque()
    
    dx = [-1,0,1,0]
    dy = [0,1,-0,-1]
    queue.append([stx,sty])
    visited[stx][sty] = True  # 시작점을 방문했음을 표시
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True  
                answer[nx][ny] = answer[x][y]+1
                queue.append([nx,ny])

bfs(goal)

for i in range(N):
    for j in range(M):
        if arr[i][j] and not answer[i][j] and arr[i][j]!=2:
            print(-1, end = " ")
        else:
            print(answer[i][j],end = " ")
    print()  

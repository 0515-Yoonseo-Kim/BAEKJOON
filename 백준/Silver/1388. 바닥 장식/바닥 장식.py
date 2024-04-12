import sys
input = sys.stdin.readline

R,C = map(int,input().split())
arr = [list(map(str,input().rstrip())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
cnt = 0

def dfs(r,c):
    visited[r][c] = True

    if arr[r][c] == "-" and c+1 < C:
        if arr[r][c] == arr[r][c+1]:
            dfs(r,c+1)
    elif arr[r][c] == "|" and r+1 < R :
        if arr[r][c] == arr[r+1][c] :
            dfs(r+1,c)

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            dfs(i,j)
            cnt+=1
            
print(cnt)


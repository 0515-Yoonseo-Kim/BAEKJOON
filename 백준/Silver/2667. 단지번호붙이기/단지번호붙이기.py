N = int(input())
arr = [[int(i) for i in input().rstrip()]for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
cnt = 0
ppl = []
def dfs(x,y):
    size = 1
    visited[x][y] = True
    if x+1 < N: 
        if arr[x+1][y] and not visited[x+1][y]:
            size += dfs(x+1,y)
    if x-1 >= 0:
        if arr[x-1][y] and not visited[x-1][y]:
            size += dfs(x-1,y)    
    if y+1 < N:
        if arr[x][y+1] and not visited[x][y+1]:
            size += dfs(x,y+1)
    if y-1 >= 0:
        if arr[x][y-1] and not visited[x][y-1]:
            size += dfs(x,y-1)
    
    return size

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt +=1
            num = dfs(i,j)
            ppl.append(num)
ppl.sort()
print(cnt)
for p in ppl:
    print(p)
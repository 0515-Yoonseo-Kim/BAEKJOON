import sys
from collections import deque
M,N,H = map(int,input().split())
moves = [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]
arr = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                queue.append((i,j,k,0))

max_d = 0

while queue:
    ci,cj,ck,cd = queue.popleft()
    for move in moves:
        ni,nj,nk = ci+move[0],cj+move[1],ck+move[2]
        if 0<=ni<H and 0<=nj<N and 0<=nk<M and arr[ni][nj][nk] == 0:
            arr[ni][nj][nk] = 1
            queue.append((ni,nj,nk,cd+1))

    max_d = max(max_d,cd)


for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                sys.exit()
print(max_d)
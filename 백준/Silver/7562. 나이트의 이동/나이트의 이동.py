from collections import deque
T = int(input())
INF = 90001
moves = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]

def bfs(st,ed):
    queue = deque([st])
    arr[st[0]][st[1]] = 0

    while queue:
        curr_r,curr_c = queue.popleft()
        curr_value = arr[curr_r][curr_c]
        if [curr_r,curr_c] == ed:
            return curr_value
        for i in range(8):
            dr,dc = moves[i]
            nr,nc = curr_r+dr, curr_c+dc
            if 0<= nr < I and 0<= nc < I and curr_value + 1 < arr[nr][nc]:
                arr[nr][nc] = curr_value + 1
                queue.append([nr,nc])
    return

for _ in range(T):
    I = int(input())
    arr = [[INF for _ in range(I)] for _ in range(I)]

    st = list(map(int,input().split()))
    ed = list(map(int,input().split()))
    print(bfs(st,ed))


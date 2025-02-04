import sys
from collections import deque
input = sys.stdin.readline

R,C = map(int,input().split())

arr = [[s for s in input().rstrip()] for _ in range(R)]
visited = [[False] * C for _ in range(R)]
moves = [(-1,0),(0,1),(1,0),(0,-1)]


def can_escape():
    queue = deque()
    jr,jc = 0,0
    for r in range(R):
        for c in range(C):
            if arr[r][c] == "J":
                jr,jc = r,c
                visited[r][c] = True
            if arr[r][c] == "F":
                queue.append([0,(r,c),arr[r][c]])
    queue.append([0,(jr,jc),arr[jr][jc]])
    while queue:
        curr_t, (curr_r, curr_c), obj = queue.popleft()
        if obj == "J":
            for dr,dc in moves:
                new_r = curr_r + dr
                new_c = curr_c + dc
                new_t = curr_t + 1
                
                if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
                    print(new_t)
                    return
                if arr[new_r][new_c] == "." and not visited[new_r][new_c]:
                    visited[new_r][new_c] = True
                    queue.append([new_t,(new_r,new_c),obj])
        else:
            for dr,dc in moves:
                new_r = curr_r + dr
                new_c = curr_c + dc
                new_t = curr_t + 1
                if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
                    continue
                if arr[new_r][new_c] != "#" and arr[new_r][new_c] != "F":
                    arr[new_r][new_c] = "F"
                    queue.append([new_t,(new_r,new_c),obj])
    print("IMPOSSIBLE")
    return

can_escape()
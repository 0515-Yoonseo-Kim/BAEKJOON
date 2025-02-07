import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(19)]

moves = [(1, 0), (0, 1), (1, 1), (1, -1)]

def check_winner(r, c, player):
    for dr, dc in moves:
        stones = [(r, c)]
        nr, nc = r + dr, c + dc

        while 0 <= nr < 19 and 0 <= nc < 19 and arr[nr][nc] == player:
            stones.append((nr, nc))
            nr += dr
            nc += dc

        
        if len(stones) == 5:
            pr, pc = r - dr, c - dc  
            nr, nc = stones[-1][0] + dr, stones[-1][1] + dc

            if (0 <= pr < 19 and 0 <= pc < 19 and arr[pr][pc] == player) or \
               (0 <= nr < 19 and 0 <= nc < 19 and arr[nr][nc] == player):
                continue
            
            stones.sort(key=lambda x: (x[1], x[0]))  
            print(player)
            print(stones[0][0] + 1, stones[0][1] + 1)
            sys.exit()


for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            check_winner(i, j, arr[i][j])

print(0)
import heapq

def solution(board):
    N = len(board)
    INF = int(1e8)
    move = [(-1,0), (0,1), (1,0), (0,-1)]
    
    dp = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    
    hq = []
    heapq.heappush(hq, (0, 0, 0, -1))

    while hq:
        cost, c, r, prev_dir = heapq.heappop(hq)

        if c == N-1 and r == N-1:
            return cost

        for i in range(4):
            nc, nr = c + move[i][0], r + move[i][1]

            if 0 <= nc < N and 0 <= nr < N and board[nc][nr] == 0:
                if prev_dir == i or prev_dir == -1:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600
                
                if new_cost < dp[nc][nr][i]:
                    dp[nc][nr][i] = new_cost
                    heapq.heappush(hq, (new_cost, nc, nr, i))

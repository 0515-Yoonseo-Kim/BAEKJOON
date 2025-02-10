import heapq

def solution(board):
    N = len(board)
    INF = float('inf')

    # 4방향 이동 (상, 우, 하, 좌)
    move = [(-1,0), (0,1), (1,0), (0,-1)]
    
    # DP 배열: [y][x][dir] 방향으로 올 때 최소 비용
    dp = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    
    # 우선순위 큐 (cost, y, x, dir)
    hq = []
    heapq.heappush(hq, (0, 0, 0, -1))  # 초기 비용 0, 시작 위치 (0,0), 방향 없음

    while hq:
        cost, y, x, prev_dir = heapq.heappop(hq)
        
        # 목표 지점 도달 시 최소 비용 반환
        if y == N-1 and x == N-1:
            return cost

        for i in range(4):  # 상우하좌 이동
            ny, nx = y + move[i][0], x + move[i][1]

            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:  # 이동 가능
                new_cost = cost + (100 if prev_dir == i or prev_dir == -1 else 600)

                # 최소 비용 갱신 시에만 진행
                if new_cost < dp[ny][nx][i]:
                    dp[ny][nx][i] = new_cost
                    heapq.heappush(hq, (new_cost, ny, nx, i))

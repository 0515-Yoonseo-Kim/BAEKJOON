def solution(m, n, puddles):
    MOD = 1_000_000_007

    # 물에 잠긴 지역을 집합으로
    puddle_set = set((y - 1, x - 1) for x, y in puddles)

    # dp[r][c]: (r, c)에서 도착점까지의 경로 수 (초기값 -1)
    dp = [[-1] * m for _ in range(n)]
    moves = [(1, 0), (0, 1)]

    def dfs(r, c):
        # 물에 잠긴 지역이면 0
        if (r, c) in puddle_set:
            return 0

        # 도착점에 도달한 경우
        if r == n - 1 and c == m - 1:
            return 1

        # 이미 계산된 경우 반환
        if dp[r][c] != -1:
            return dp[r][c]

        total = 0
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                total = (total + dfs(nr, nc)) % MOD

        dp[r][c] = total
        return dp[r][c]

    return dfs(0, 0)

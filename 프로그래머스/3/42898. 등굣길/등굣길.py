# 최단경로를 찾는게 아닌 최단경로의 개수를 찾는 문제 -> dfs 분할 정복 문제로 해결
# 맨왼쪽위에서부터 맨오른쪽아래로 정해져있고 이동방향은 오른쪽과 밑만 가능
# 물에 잠긴 지역은 최대 10개이지만 매번 확인해줘야하기 때문에 set로 탐색.
def dfs(r,c):
    if r==n-1 and c==m-1:
        return 1
    for dr,dc in moves:
        nr,nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m:
            cnt += dfs(nr,nc)
        else:
            return 0
    
    return 
def solution(m, n, puddles):
    MOD = 1000000007
    puddle_set = set((y - 1, x - 1) for x, y in puddles)
    moves = [[1,0],[0,1]]
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    def dfs(r,c):
        if (r,c) in puddle_set:
            return 0
        
        if r == n-1 and c == m-1:
            return 1
        
        if dp[r][c] != 0:
            return dp[r][c]

        total = 0
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                total = (total + dfs(nr, nc)) % MOD

        dp[r][c] = total
        return dp[r][c]
    
    return dfs(0,0)
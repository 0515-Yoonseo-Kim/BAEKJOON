import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# DP 배열 선언 (-1은 아직 계산되지 않은 경우)
dp = [[[-1] * N for _ in range(N)] for _ in range(3)]

# 대각선 이동 체크 함수
def cross_move(x, y):
    return is_empty(x + 1, y + 1) and is_empty(x, y + 1) and is_empty(x + 1, y)

# 빈 칸 체크
def is_empty(x, y):
    return 0 <= x < N and 0 <= y < N and arr[x][y] == 0

def dfs(status, x, y):

    if x == N - 1 and y == N - 1:
        return 1

    if dp[status][x][y] != -1:
        return dp[status][x][y]

    dp[status][x][y] = 0  # 초기화

    # 가로 이동
    if status == 0 or status == 1:
        if is_empty(x, y + 1):
            dp[status][x][y] += dfs(0, x, y + 1)

    # 세로 이동
    if status == 1 or status == 2:
        if is_empty(x + 1, y):
            dp[status][x][y] += dfs(2, x + 1, y)

    # 대각선 이동
    if cross_move(x, y):
        dp[status][x][y] += dfs(1, x + 1, y + 1)

    return dp[status][x][y]

print(dfs(0, 0, 1))

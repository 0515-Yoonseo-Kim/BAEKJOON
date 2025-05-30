import sys
input = sys.stdin.readline

INF = int(1e9)
MAX = 301

# 플로이드-워셜 알고리즘
def floyd_warshall(dp, n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

# 정답 찾기 / 시간 복잡도를 위해서 기존 dp에서 경로를 업데이트 했을때에 줄어드는 경우가 있는지 확인.
def find_answer(dp, s, t, a1, b1, c1, a2, b2, c2):
    answer = dp[s][t]
    answer = min(answer, dp[s][a1] + min(c1, dp[a1][b1]) + dp[b1][t])
    answer = min(answer, dp[s][a2] + min(c2, dp[a2][b2]) + dp[b2][t])
    answer = min(answer, dp[s][a1] + min(c1, dp[a1][b1]) + dp[b1][a2] + min(c2, dp[a2][b2]) + dp[b2][t])
    answer = min(answer, dp[s][a2] + min(c2, dp[a2][b2]) + dp[b2][a1] + min(c1, dp[a1][b1]) + dp[b1][t])
    return answer if answer != INF else -1



dp = [[INF] * MAX for _ in range(MAX)]
for i in range(MAX):
    dp[i][i] = 0
N,M,S,T= map(int, input().split())
for _ in range(M):
    u, v, w = map(int, input().split())
    dp[u][v] = min(dp[u][v], w)

floyd_warshall(dp,N)

# 시나리오 처리
q = int(input())
for _ in range(q):
    a1, b1, c1, a2, b2, c2 = map(int, input().split())
    answer = find_answer(dp, S, T, a1, b1, c1, a2, b2, c2)
    print(answer)

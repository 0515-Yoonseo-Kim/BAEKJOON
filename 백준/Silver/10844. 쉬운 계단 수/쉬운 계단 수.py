# 백준 : 간단한 계단수
N = int(input())

dp = [[0]*10 for _ in range(101)]
for j in range(1,10):
    dp[1][j] = 1

for i in range(2,N+1):
    for j in range(10):
        if 0<j<9:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
        elif j == 0:
            dp[i][j]=dp[i-1][j+1]
        else:
            dp[i][j]=dp[i-1][j-1]

print(sum(dp[N])%1000000000)


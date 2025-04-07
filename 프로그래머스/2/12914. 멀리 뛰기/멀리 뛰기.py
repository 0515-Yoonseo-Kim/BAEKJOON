# 순서 없음
def solution(n):
    if n == 1 or n == 2:
        return n
    dp = [0]*2001
    dp[1],dp[2] = 1,2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]%1234567
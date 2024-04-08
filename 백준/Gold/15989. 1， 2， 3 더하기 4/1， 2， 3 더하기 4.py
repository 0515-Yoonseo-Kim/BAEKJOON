import sys
sys.stdin.readline

T = int(input())
dp = [1]*10001
for i in range(2,4):
    for j in range(1,10001):
        if j>=i:
            dp[j] += dp[j-i]

for _ in range(T):
    N = int(input())
    print(dp[N])

    
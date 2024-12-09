N = int(input())
num_li = list(map(int,input().split()))
dp = [1 for _ in range(N)]
dp[0] = 1

for i in range(N):
    for j in range(i):
        if num_li[i] > num_li[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
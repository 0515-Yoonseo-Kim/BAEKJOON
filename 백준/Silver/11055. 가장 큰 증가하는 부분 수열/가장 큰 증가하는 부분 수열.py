N = int(input())
num_li  = list(map(int,input().split()))
dp = [0]*(N+1)

for i in range(N):
    for j in range(i):
        if num_li[i]>num_li[j]:
            dp[i]=max(dp[i],dp[j])
    dp[i]+=num_li[i]

print(max(dp))
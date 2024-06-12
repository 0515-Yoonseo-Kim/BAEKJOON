def fibonacci(n):
    dp = [0]*(41)
    dp[0],dp[1]=1,1
    if n == 1 or n==2:
        return n
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    
    return dp[n]

N = int(input())
M = int(input())

cnt = []
temp = 0
for _ in range(M):
    fixed = int(input())
    cnt.append(fixed-temp-1)
    temp = fixed
cnt.append(N-temp)


way = list(map(fibonacci,cnt))
answer = 1

for i in way:
    answer*=i

print(answer)

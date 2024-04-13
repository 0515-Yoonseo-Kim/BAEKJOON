N,K = map(int,input().split())
coins = [int(input()) for i in range(N)]
arr = [0]*(K+1)
arr[0]=1
coins.sort()

for coin in coins:
    for i in range(coin,K+1):
        arr[i]+=arr[i-coin]

print(arr[-1])


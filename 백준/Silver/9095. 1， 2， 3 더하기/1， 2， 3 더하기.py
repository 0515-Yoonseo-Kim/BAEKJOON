T = int(input())

for _ in range(T):
    N = int(input())
    arr = [0]*(N+1)
    arr[0] = 1
    for i in range(N+1):
        if i-1>=0:
            arr[i]+=arr[i-1]
        if i-2>=0:
            arr[i]+=arr[i-2]
        if i-3>=0:
            arr[i]+=arr[i-3]
    print(arr[-1])

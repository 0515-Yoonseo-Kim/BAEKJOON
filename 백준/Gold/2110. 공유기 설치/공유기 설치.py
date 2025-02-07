N, C = map(int,input().split())

arr = sorted([int(input()) for _ in range(N)])

left,right = 1, arr[-1] - arr[0]
ans = 0

while left <= right:
    mid = (left + right) // 2
    prev = arr[0]
    cnt = 1

    for i in range(1,N):
        if arr[i] - prev >= mid:
            cnt += 1
            prev = arr[i]

    if cnt >= C:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
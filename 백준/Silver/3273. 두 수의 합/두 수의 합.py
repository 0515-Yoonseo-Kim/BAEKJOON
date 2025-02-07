N = int(input())
num_li = sorted(list(map(int, input().split())))
x = int(input())

left, right = 0, N - 1
cnt = 0

while left < right:
    now = num_li[left] + num_li[right]
    if now == x:
        cnt += 1
        left += 1
        right -= 1
    elif now < x:
        left += 1
    else:
        right -= 1

print(cnt)

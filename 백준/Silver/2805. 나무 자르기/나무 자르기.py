N, M = map(int,input().split())
trees = list(map(int,input().split()))
left, right = 0, max(trees)

while left + 1 < right:
    mid = (left+right)//2
    temp = sum(list(map(lambda x: max(0,x-mid),trees)))

    if temp >= M:
        left = mid
    else:
        right = mid
print(left)
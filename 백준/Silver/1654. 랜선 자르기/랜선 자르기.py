import sys
input = sys.stdin.readline

K,N = map(int,input().split())
lines = [int(input()) for _ in range(K)]

l,r = 1, max(lines)
result = 0

while l<=r:
    mid = (l+r)//2
    cnt = sum([line//mid for line in lines])
    
    if cnt >= N:
        result = mid
        l = mid + 1
    else:
        r = mid - 1
print(result)
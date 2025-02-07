import sys
import bisect
input = sys.stdin.readline

min_value = int(2*1e9)

N, M = map(int,input().split())
arr = sorted([int(input()) for _ in range(N)])

for i in range(N):
    idx = bisect.bisect_left(arr,arr[i] + M)
    if idx < N:
        min_value = min(min_value,arr[idx]-arr[i])
print(min_value)
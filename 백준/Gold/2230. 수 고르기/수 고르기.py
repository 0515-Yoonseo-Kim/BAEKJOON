import sys
import heapq
input = sys.stdin.readline

N, M = map(int,input().split())
arr = sorted([int(input()) for _ in range(N)])
left, right = 0, 0
min_val =  int(2*1e9)

while left < N:
    if right == N:
        break
    if arr[right]- arr[left] < M:
        right += 1
        continue
    min_val = min(min_val,arr[right]-arr[left])
    left += 1
print(min_val)
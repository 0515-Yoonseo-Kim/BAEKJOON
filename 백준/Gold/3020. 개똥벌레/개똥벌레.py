import sys
from collections import defaultdict
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
N,H = map(int,input().split())

bottom,top=[],[]

for i in range(N):
    if i%2 == 0:
        bottom.append(int(input()))
    else:
        top.append(H-int(input()))
# 구하는 것 : 부수는 장애물의 최소 개수, 경우의 수
bottom.sort()
top.sort()

total_dict = defaultdict(int)
min_val = N
for h in range(H):
    bottom_sum = len(bottom)-bisect_right(bottom,h)
    top_sum = bisect_left(top,h+1)
    total_sum = bottom_sum+top_sum
    total_dict[total_sum]+=1
    min_val = min(min_val, total_sum)


print(min_val,total_dict[min_val])    


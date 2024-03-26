import sys
import heapq

input=sys.stdin.readline
N = int(input())

road_list = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):  
            if road_list[a][k] and road_list[k][b]:
                road_list[a][b] = 1

for row in road_list:
    print(*row)
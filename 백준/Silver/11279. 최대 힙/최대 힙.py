import heapq,sys
input = sys.stdin.readline

queue = []
N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if not queue:
            print(0)
        else:
            print(-heapq.heappop(queue))
    heapq.heappush(queue,-num)
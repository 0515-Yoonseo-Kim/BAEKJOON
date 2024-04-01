import sys
import heapq
input = sys.stdin.readline

N = int(input())
schedule = []
for _ in range(N):
    sch = list(map(int,input().split()))
    schedule.append(sch)
schedule.sort()

cnt = 1
end = []
heapq.heappush(end,schedule[0][1])
for i in range(1,N):
    s,e = schedule[i]
    compare = heapq.heappop(end)
    if s<compare:
        heapq.heappush(end,compare)
        heapq.heappush(end,e)
        cnt+=1
    else:
        heapq.heappush(end,e)
print(cnt)
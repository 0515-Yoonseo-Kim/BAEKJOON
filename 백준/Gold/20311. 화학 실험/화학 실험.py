import heapq

N,K = map(int,input().split())
nums = list(map(int,input().split()))

max_heap = []
for num, cnt in enumerate(nums,start=1):
    heapq.heappush(max_heap,[-cnt,num])

answer = []

while max_heap:
    curr_cnt, curr_num = heapq.heappop(max_heap)

    if curr_cnt == 0:
        continue

    if answer and curr_num == answer[-1]:
        if not max_heap:
            break
        next_cnt, next_num = heapq.heappop(max_heap)
        answer.append(next_num)
        heapq.heappush(max_heap,[next_cnt+1,next_num])
        heapq.heappush(max_heap,[curr_cnt, curr_num])
        continue

    answer.append(curr_num)
    curr_cnt = -(curr_cnt) - 1

    if curr_cnt > 0:
        heapq.heappush(max_heap,[-curr_cnt,curr_num])
if len(answer) == N:
    print(*answer,end=" ")
else:
    print(-1)
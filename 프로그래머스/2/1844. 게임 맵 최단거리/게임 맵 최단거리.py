# 왼쪽상단끝 -> 오른쪽하단끝
# 1 -> 지나갈 수 있음 / 0 -> 지나갈 수 없음
# 가장 빠른 거리 return -> heapq 사용해서 도착 즉시 거리 return
# n -> 행, m -> 열 다를 수도 있음
# visited도 필요할 듯?
import heapq
def solution(maps):
    N,M = len(maps), len(maps[0])
    di = [[0,1],[1,0],[0,-1],[-1,0]]
    queue = []
    heapq.heappush(queue, [1,(0,0)])
    while queue:
        cnt, (curr_r,curr_c) = heapq.heappop(queue)
        if (curr_r,curr_c) == (N-1,M-1):
            return cnt
        for i in range(4):
            nr, nc = curr_r + di[i][0], curr_c + di[i][1]
            if 0<=nr<N and 0<=nc<M and maps[nr][nc] == 1:
                maps[nr][nc] += 1
                heapq.heappush(queue,[cnt+1,(nr,nc)])
    return -1
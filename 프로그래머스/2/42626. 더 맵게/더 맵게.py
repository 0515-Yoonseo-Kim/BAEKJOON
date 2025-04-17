# 가장 낮은 두 개의 음식 섞어서 새로운 음식
# 가장 맵지 않은 것 + 두번째로 맵지 않은 것 * 2
# 모든것이 K 이상이 될때까지 반복해서 섞음.
from typing import List
import heapq
def mix_food(f1: int,f2: int) -> int:
    return f1+2*f2
def solution(scoville: List[int], K: int) -> int:
    heapq.heapify(scoville)
    cnt = 0
    while True:
        now = heapq.heappop(scoville)
        if now >= K:
            return cnt
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville,mix_food(now,second))
        cnt += 1
    return -1
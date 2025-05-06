# 가장 작업량이 많은 일부터 해야함. -> 우선순위 큐 자료구조 사용
import heapq
def solution(n, works):
    works = [-w for w in works]
    heapq.heapify(works)
    while n>0:
        now = heapq.heappop(works)
        if now == 0:
            break
        heapq.heappush(works,now+1)
        n -= 1

    return sum(map(lambda x: x**2, works))